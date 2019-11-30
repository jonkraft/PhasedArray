"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
import time
import spidev
from gnuradio import gr
import sys

try:
    import iio
except:
    sys.path.append('/usr/lib/python2.7/site-packages/')
    try:
        import iio
    except:
        print("IIO library is not installed.  Download from https://github.com/analogdevicesinc/libad9361-iio.git")
        sys.exit(0)

"""install the pyadi-iio python libs
sudo pip install pyadi-iio
https://analogdevicesinc.github.io/pyadi-iio/"""

try:
    import adi
except:
    print("PYADI-IIO not installed.  Download rev 0.0.2 at https://pypi.org/project/pyadi-iio/0.0.2/#files")
    print("IIO lib will be used instead")
    

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block

    def __init__(self, LO_freq=2400000000, TX_freq=5810000000, SampleRate=3000000, Rx_gain=30, Averages=1, Taper=1, SymTaper=0, PhaseCal=0, SignalFreq=10525000000, RxGain1=127, RxGain2=127, RxGain3=127, RxGain4=127, Rx1_cal=0, Rx2_cal=0, Rx3_cal=0, Rx4_cal=0):  
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='ADAR1000 Sweeper',   # will show up in GRC
            in_sig=[],
            out_sig=[np.complex64, np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.LO_freq = LO_freq              # RX LO freq
        self.TX_freq = TX_freq              # TX LO freq
        self.SampleRate = SampleRate
        self.Rx_gain = Rx_gain
        self.Averages = Averages
        self.Taper = Taper
        self.SymTaper = SymTaper
        self.PhaseCal = PhaseCal
        self.RxGain1 = RxGain1
        self.RxGain2 = RxGain2
        self.RxGain3 = RxGain3
        self.RxGain4 = RxGain4
        self.Rx1_cal=Rx1_cal
        self.Rx2_cal=Rx2_cal
        self.Rx3_cal=Rx3_cal
        self.Rx4_cal=Rx4_cal
                       
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)  #set bus=0 and device=0
        self.spi.max_speed_hz = 500000
        self.spi.mode = 0
        
        self.c = 299792458    # speed of light in m/s
        self.d = 0.015        # element to element spacing of the antenna
        self.f = SignalFreq
        
        #By default, pluto captures 4 buffers of data.  I need to change that to 1, otherwise I'll be out of sync with my spi writes
        #The new version of adi.py will do this, but I can't use the new version because it doesn't support Python2
        #And I need to use Python2, because that is what GNUradio uses (though if I upgrade to GNUradio3.8, then I could use Python3)
        #So, as a patch, I change buffer count use iio.py library
        ctx=iio.Context('ip:192.168.2.1')
        txdac = ctx.find_device("cf-ad9361-dds-core-lpc")
        rxadc = ctx.find_device("cf-ad9361-lpc")
        self.ctrl = ctx.find_device("ad9361-phy")
        self.rx = self.ctrl.find_channel("voltage0")
        #self.rx.attrs["sampling_frequency"].value = str(int(40000000))
        self.rx.attrs["quadrature_tracking_en"].value = str(0)   # we are receiving a real (not complex) signal.  Therefore disable QEC, or that tracking loop will cause amplitude variation
        try:
            rxadc.set_kernel_buffers_count(int(1))    #This parameter doesn't like to be set too often....  So sometimes it gives an error
        except:
            print("No change to buffer count")

        self.adi_install=True
        try:     #if pyadi-iio (rev 0.0.2) is installed, then use that.  It's nice and clean.  Otherwise we'll use the slightly harder to decipher iio.lib
            #https://analogdevicesinc.github.io/pyadi-iio/#module-adi.ad9361
            #sdr=adi.Pluto()     #This finds pluto over usb.  But communicating with its ip address gives us more flexibility
            self.sdr=adi.Pluto(uri='ip:192.168.2.1')      #This finds the device at that ip address
            #sdr._rxadc.set_kernel_buffers_count=1         #This doesn't work in adi.py 0.0.2 as discussed above
            self.sdr.sample_rate = int(self.SampleRate)
            #self.sdr.filter = "/home/pi/Documents/PlutoFilters/samprate_40p0.ftr"  #pyadi-iio auto applies filters based on sample rate
            #self.sdr.rx_rf_bandwidth = int(1000000)
            #self.sdr.tx_rf_bandwidth = int(500000)
            self.sdr.rx_buffer_size = int(4*256)
            self.sdr.tx_lo = int(self.TX_freq)
            self.sdr.tx_cyclic_buffer = True
            self.sdr.tx_buffer_size = int(2**18)
            self.sdr.tx_hardwaregain = -3
            self.sdr.dds_enabled = [1, 1, 1, 1]                  #DDS generator enable state
            self.sdr.dds_frequencies = [0.1e6, 0.1e6, 0.1e6, 0.1e6]      #Frequencies of DDSs in Hz
            self.sdr.dds_scales = [1, 1, 0, 0]                   #Scale of DDS signal generators Ranges [0,1]            
            self.sdr.gain_control_mode = "manual"                #We must be in manual gain control mode (otherwise we won't see the peaks and nulls!)
            
        except:      # if pyadi-iio isn't installed, then we'll just use the iio.lib to do it.  It's a bit longer and clunkier though....
            try:
                print("Using IIO.lib (instead of adipy-iio library)")
                self.adi_install=False
              
                # Configure transceiver settings
                self.rxLO = self.ctrl.find_channel("altvoltage0", True)
                self.txLO = self.ctrl.find_channel("altvoltage1", True)
                self.txLO.attrs["frequency"].value = str(int(self.TX_freq))

                self.tx = self.ctrl.find_channel("voltage0",True)
                self.tx.attrs["rf_bandwidth"].value = str(int(500000))
                self.tx.attrs["sampling_frequency"].value = str(int(self.SampleRate))
                self.tx.attrs['hardwaregain'].value = '-3'

                self.rx.attrs["rf_bandwidth"].value = str(int(self.SampleRate/2))
                self.rx.attrs["sampling_frequency"].value = str(int(self.SampleRate))
                self.rx.attrs['gain_control_mode'].value = 'manual'

                # Enable all IQ channels
                rxadc.find_channel("voltage0").enabled = True
                rxadc.find_channel("voltage1").enabled = True
                txdac.find_channel("voltage0",True).enabled = True
                txdac.find_channel("voltage1",True).enabled = True
                
                # Force DAC to use DDS not DMA
                dds0 = txdac.find_channel('TX1_I_F1',True)
                dds2 = txdac.find_channel('TX1_Q_F1',True)
                dds1 = txdac.find_channel('TX1_I_F2',True)
                dds3 = txdac.find_channel('TX1_Q_F2',True)

                # Enable single tone DDS
                dds0.attrs['raw'].value = str(1)
                dds0.attrs['frequency'].value = str(0.1e6)
                dds0.attrs['scale'].value = str(1)
                dds0.attrs['phase'].value = str(90000)
                dds2.attrs['raw'].value = str(1)
                dds2.attrs['frequency'].value = str(0.1e6)
                dds2.attrs['scale'].value = str(1)
                dds2.attrs['phase'].value = str(0)
                
                dds1.attrs['raw'].value = str(0)
                dds1.attrs['frequency'].value = str(0.1e6)
                dds1.attrs['scale'].value = str(1)
                dds1.attrs['phase'].value = str(90000)
                dds3.attrs['raw'].value = str(0)
                dds3.attrs['frequency'].value = str(0.1e6)
                dds3.attrs['scale'].value = str(0.0)
                dds3.attrs['phase'].value = str(0)

                # Create buffer for RX data
                self.rxbuf = iio.Buffer(rxadc, int(2*256), False)

                # Create cyclic buffer for TX data
                samples_per_channel = 2**18
                try:
                    txbuf = iio.Buffer(txdac, samples_per_channel, True)
                except:
                    print("Error.  Could not create Tx buffer")     # If the IIO GNUradio block is run before this script, then the Txbuffer can have trouble
                    print("Unplug Plugo, wait 10 sec, then plug back in.")  # There must be a better way to destroy the buffer in iio.py???
                    sys.exit(0)
                    
            except:
                    print("Error.  Could not create Pluto Python objects.")     # If the IIO GNUradio block is run before this script, then the Txbuffer can have trouble
                    print("Unplug Plugo, wait 10 sec, then plug back in.")  # There must be a better way to destroy the buffer in iio.py???
                    sys.exit(0)

    def work(self, input_items, output_items):
        if self.adi_install == True:         # If pyadi-iio is installed, then use that.  It's easier, cleaner, etc.
            self.sdr.rx_lo = int(self.LO_freq)
            self.sdr.rx_hardwaregain = int(self.Rx_gain)
            #print("RX LO %s" % (self.sdr.rx_lo))   # read out the programmed Rx LO frequency

        else:                                # No pyadi-iio??  No problem!  We'll use iio.py library instead
            self.rxLO.attrs["frequency"].value = str(int(self.LO_freq))
            self.rx.attrs['hardwaregain'].value = str(int(self.Rx_gain))
            
        # The ADDR is set by the address pins on the ADAR1000.  This is set by P10 on the eval board.
        ADDR1=0x20            # ADDR 0x20 is set by jumpering pins 4 and 6 on P10
        #ADDR1=0x00           # ADDR 0x00 is set by leaving all jumpers off of P10

        if self.Taper==0:
            # set the ADAR1000's VGA gain of each of the Rx channels.  RxGainx needs to be between 0 and 127
            self.spi.xfer2([ADDR1, 0x10, int(np.minimum(self.RxGain1*128, 128)+self.RxGain1)])  # Sets Rx1 VGA gain.  If gain =0, then also kick in the 20dB attenuator
            self.spi.xfer2([ADDR1, 0x11, int(np.minimum(self.RxGain2*128, 128)+self.RxGain2)])  # Sets Rx2 VGA gain.  If gain =0, then also kick in the 20dB attenuator
            self.spi.xfer2([ADDR1, 0x12, int(np.minimum(self.RxGain3*128, 128)+self.RxGain3)])  # Sets Rx3 VGA gain.  If gain =0, then also kick in the 20dB attenuator
            if self.SymTaper==0:
                self.spi.xfer2([ADDR1, 0x13, int(np.minimum(self.RxGain4*128, 128)+self.RxGain4)])  # Sets Rx4 VGA gain.  If gain =0, then also kick in the 20dB attenuator
            else:
                self.spi.xfer2([ADDR1, 0x13, int(np.minimum(self.RxGain1*128, 128)+self.RxGain1)])  # If Symmetric Taper is set high, then make Rx4 gain equal to Rx1 gain
        else:
            self.spi.xfer2([ADDR1, 0x10, int(128+127)])  # Sets Rx1 VGA gain
            self.spi.xfer2([ADDR1, 0x11, int(128+127)])  # Sets Rx2 VGA gain
            self.spi.xfer2([ADDR1, 0x12, int(128+127)])  # Sets Rx3 VGA gain
            self.spi.xfer2([ADDR1, 0x13, int(128+127)])  # Sets Rx4 VGA gain

        PhaseValues = np.arange(-196.875, 196.875, 2.8125)   # These are all the phase deltas (i.e. phase difference between Rx1 and Rx2, then Rx2 and Rx3, etc.) we'll sweep.     
        PhaseStepNumber=0    # this is the number of phase steps we'll take (140 in total).  At each phase step, we set the individual phases of each of the Rx channels
        max_signal = -100    # Reset max_signal.  We'll keep track of the maximum signal we get as we do this 140 loop.  
        max_angle = 0        # Reset max_angle.  This is the angle where we saw the max signal.  This is where our compass will point.
        
        if self.PhaseCal == 0:
            Rx1_Phase_Cal = self.Rx1_cal
            Rx2_Phase_Cal = self.Rx2_cal
            Rx3_Phase_Cal = self.Rx3_cal
            Rx4_Phase_Cal = self.Rx4_cal
        else:
            Rx1_Phase_Cal = 0
            Rx2_Phase_Cal = 0
            Rx3_Phase_Cal = 0
            Rx4_Phase_Cal = 0
        
        for PhDelta in PhaseValues:
            # steering angle theta = arcsin(c*deltaphase/(2*pi*f*d)
            # if element spacing is lambda/2 then this simplifies to theta=arcsin(deltaphase(in radians)/pi)
            value1 = (self.c * np.radians(np.abs(PhDelta)))/(2*3.14159*self.f*self.d)
            clamped_value1 = max(min(1, value1), -1)     #arcsin argument must be between 1 and -1, or numpy will throw a warning
            theta = np.degrees(np.arcsin(clamped_value1))
            if PhDelta>=0:
                SteerAngle = 90 + theta   # positive PhaseDelta covers 0deg to 90 deg
                Phase_A = (np.abs(PhDelta*0) + Rx4_Phase_Cal) % 360
                Phase_B = (np.abs(PhDelta*1) + Rx3_Phase_Cal) % 360
                Phase_C = (np.abs(PhDelta*2) + Rx2_Phase_Cal) % 360
                Phase_D = (np.abs(PhDelta*3) + Rx1_Phase_Cal) % 360
                channels = [Phase_D, Phase_C, Phase_B, Phase_A]  # if PhaseDelta is positive, then signal source is to the right, so Rx1 needs to be delayed the most
            else:
                SteerAngle = 90 - theta # negative phase delta covers 0 deg to -90 deg
                Phase_A = (np.abs(PhDelta*0) + Rx1_Phase_Cal) % 360
                Phase_B = (np.abs(PhDelta*1) + Rx2_Phase_Cal) % 360
                Phase_C = (np.abs(PhDelta*2) + Rx3_Phase_Cal) % 360
                Phase_D = (np.abs(PhDelta*3) + Rx4_Phase_Cal) % 360  
                channels = [Phase_A, Phase_B, Phase_C, Phase_D]  #  if PhaseDelta is negative, then signal source is to the left, so Rx4 needs to be delayed the most

            # Write vector I and Q to set phase shift (see Table 13 in ADAR1000 datasheet)
            i=1
            for Channel_Phase in channels:
                if i==1:
                    I = 0x14   # Rx1_I vector register address = 0x14
                    Q = 0x15   # Rx1_Q vector register address = 0x15
                    ADDR=ADDR1
                if i==2:
                    I = 0x16   # Rx2_I vector register address = 0x16
                    Q = 0x17   # Rx2_Q vector register address = 0x17
                    ADDR=ADDR1
                if i==3:
                    I = 0x18   # Rx3_I vector register address = 0x18
                    Q = 0x19   # Rx3_Q vector register address = 0x19
                    ADDR=ADDR1
                if i==4:
                    I = 0x1A   # Rx4_I vector register address = 0x1A
                    Q = 0x1B   # Rx4_Q vector register address = 0x1B
                    ADDR=ADDR1
                i = i+1
                          
                # Quadrant 1
                if Channel_Phase==0:
                    self.spi.xfer2([ADDR, I, 0x3F])
                    self.spi.xfer2([ADDR, Q, 0x20])
                if Channel_Phase==2.8125:
                    self.spi.xfer2([ADDR, I, 0x3F])
                    self.spi.xfer2([ADDR, Q, 0x21])
                if Channel_Phase==5.625:
                    self.spi.xfer2([ADDR, I, 0x3F])
                    self.spi.xfer2([ADDR, Q, 0x23])
                if Channel_Phase==8.4375:
                    self.spi.xfer2([ADDR, I, 0x3F])
                    self.spi.xfer2([ADDR, Q, 0x24])
                if Channel_Phase==11.25:
                    self.spi.xfer2([ADDR, I, 0x3F])
                    self.spi.xfer2([ADDR, Q, 0x26])
                if Channel_Phase==14.0625:
                    self.spi.xfer2([ADDR, I, 0x3E])
                    self.spi.xfer2([ADDR, Q, 0x27])
                if Channel_Phase==16.875:
                    self.spi.xfer2([ADDR, I, 0x3E])
                    self.spi.xfer2([ADDR, Q, 0x28])
                if Channel_Phase==19.6875:
                    self.spi.xfer2([ADDR, I, 0x3D])
                    self.spi.xfer2([ADDR, Q, 0x2A])
                if Channel_Phase==22.5:
                    self.spi.xfer2([ADDR, I, 0x3D])
                    self.spi.xfer2([ADDR, Q, 0x2B])
                if Channel_Phase==25.3125:
                    self.spi.xfer2([ADDR, I, 0x3C])
                    self.spi.xfer2([ADDR, Q, 0x2D])
                if Channel_Phase==28.125:
                    self.spi.xfer2([ADDR, I, 0x3C])
                    self.spi.xfer2([ADDR, Q, 0x2E])
                if Channel_Phase==30.9375:
                    self.spi.xfer2([ADDR, I, 0x3B])
                    self.spi.xfer2([ADDR, Q, 0x2F])
                if Channel_Phase==33.75:
                    self.spi.xfer2([ADDR, I, 0x3A])
                    self.spi.xfer2([ADDR, Q, 0x30])
                if Channel_Phase==36.5625:
                    self.spi.xfer2([ADDR, I, 0x39])
                    self.spi.xfer2([ADDR, Q, 0x31])
                if Channel_Phase==39.375:
                    self.spi.xfer2([ADDR, I, 0x38])
                    self.spi.xfer2([ADDR, Q, 0x33])
                if Channel_Phase==42.1875:
                    self.spi.xfer2([ADDR, I, 0x37])
                    self.spi.xfer2([ADDR, Q, 0x34])
                if Channel_Phase==45:
                    self.spi.xfer2([ADDR, I, 0x36])
                    self.spi.xfer2([ADDR, Q, 0x35])
                if Channel_Phase==47.8125:
                    self.spi.xfer2([ADDR, I, 0x35])
                    self.spi.xfer2([ADDR, Q, 0x36])
                if Channel_Phase==50.625:
                    self.spi.xfer2([ADDR, I, 0x34])
                    self.spi.xfer2([ADDR, Q, 0x37])
                if Channel_Phase==53.4375:
                    self.spi.xfer2([ADDR, I, 0x33])
                    self.spi.xfer2([ADDR, Q, 0x38])
                if Channel_Phase==56.25:
                    self.spi.xfer2([ADDR, I, 0x32])
                    self.spi.xfer2([ADDR, Q, 0x38])
                if Channel_Phase==59.0625:
                    self.spi.xfer2([ADDR, I, 0x30])
                    self.spi.xfer2([ADDR, Q, 0x39])
                if Channel_Phase==61.875:
                    self.spi.xfer2([ADDR, I, 0x2F])
                    self.spi.xfer2([ADDR, Q, 0x3A])
                if Channel_Phase==64.6875:
                    self.spi.xfer2([ADDR, I, 0x2E])
                    self.spi.xfer2([ADDR, Q, 0x3A])
                if Channel_Phase==67.5:
                    self.spi.xfer2([ADDR, I, 0x2C])
                    self.spi.xfer2([ADDR, Q, 0x3B])
                if Channel_Phase==70.3125:
                    self.spi.xfer2([ADDR, I, 0x2B])
                    self.spi.xfer2([ADDR, Q, 0x3C])
                if Channel_Phase==73.125:
                    self.spi.xfer2([ADDR, I, 0x2A])
                    self.spi.xfer2([ADDR, Q, 0x3C])
                if Channel_Phase==75.9375:
                    self.spi.xfer2([ADDR, I, 0x28])
                    self.spi.xfer2([ADDR, Q, 0x3C])
                if Channel_Phase==78.75:
                    self.spi.xfer2([ADDR, I, 0x27])
                    self.spi.xfer2([ADDR, Q, 0x3D])
                if Channel_Phase==81.5625:
                    self.spi.xfer2([ADDR, I, 0x25])
                    self.spi.xfer2([ADDR, Q, 0x3D])
                if Channel_Phase==84.375:
                    self.spi.xfer2([ADDR, I, 0x24])
                    self.spi.xfer2([ADDR, Q, 0x3D])
                if Channel_Phase==87.1875:
                    self.spi.xfer2([ADDR, I, 0x22])
                    self.spi.xfer2([ADDR, Q, 0x3D])
                    
            # Quadrant 2
                if Channel_Phase==90:
                    self.spi.xfer2([ADDR, I, 0x21])
                    self.spi.xfer2([ADDR, Q, 0x3D])
                if Channel_Phase==92.8125:
                    self.spi.xfer2([ADDR, I, 0x01])
                    self.spi.xfer2([ADDR, Q, 0x3D])
                if Channel_Phase==95.625:
                    self.spi.xfer2([ADDR, I, 0x03])
                    self.spi.xfer2([ADDR, Q, 0x3D])
                if Channel_Phase==98.4375:
                    self.spi.xfer2([ADDR, I, 0x04])
                    self.spi.xfer2([ADDR, Q, 0x3D])
                if Channel_Phase==101.25:
                    self.spi.xfer2([ADDR, I, 0x06])
                    self.spi.xfer2([ADDR, Q, 0x3D])
                if Channel_Phase==104.0625:
                    self.spi.xfer2([ADDR, I, 0x07])
                    self.spi.xfer2([ADDR, Q, 0x3C])
                if Channel_Phase==106.875:
                    self.spi.xfer2([ADDR, I, 0x08])
                    self.spi.xfer2([ADDR, Q, 0x3C])
                if Channel_Phase==109.6875:
                    self.spi.xfer2([ADDR, I, 0x0A])
                    self.spi.xfer2([ADDR, Q, 0x3C])
                if Channel_Phase==112.5:
                    self.spi.xfer2([ADDR, I, 0x0B])
                    self.spi.xfer2([ADDR, Q, 0x3B])
                if Channel_Phase==115.3125:
                    self.spi.xfer2([ADDR, I, 0x0D])
                    self.spi.xfer2([ADDR, Q, 0x3A])
                if Channel_Phase==118.125:
                    self.spi.xfer2([ADDR, I, 0x0E])
                    self.spi.xfer2([ADDR, Q, 0x3A])
                if Channel_Phase==120.9375:
                    self.spi.xfer2([ADDR, I, 0x0F])
                    self.spi.xfer2([ADDR, Q, 0x39])
                if Channel_Phase==123.75:
                    self.spi.xfer2([ADDR, I, 0x11])
                    self.spi.xfer2([ADDR, Q, 0x38])
                if Channel_Phase==126.5625:
                    self.spi.xfer2([ADDR, I, 0x12])
                    self.spi.xfer2([ADDR, Q, 0x38])
                if Channel_Phase==129.375:
                    self.spi.xfer2([ADDR, I, 0x13])
                    self.spi.xfer2([ADDR, Q, 0x37])
                if Channel_Phase==132.1875:
                    self.spi.xfer2([ADDR, I, 0x14])
                    self.spi.xfer2([ADDR, Q, 0x36])
                if Channel_Phase==135:
                    self.spi.xfer2([ADDR, I, 0x16])
                    self.spi.xfer2([ADDR, Q, 0x35])
                if Channel_Phase==137.8125:
                    self.spi.xfer2([ADDR, I, 0x17])
                    self.spi.xfer2([ADDR, Q, 0x34])
                if Channel_Phase==140.625:
                    self.spi.xfer2([ADDR, I, 0x18])
                    self.spi.xfer2([ADDR, Q, 0x33])
                if Channel_Phase==143.4375:
                    self.spi.xfer2([ADDR, I, 0x19])
                    self.spi.xfer2([ADDR, Q, 0x31])
                if Channel_Phase==146.25:
                    self.spi.xfer2([ADDR, I, 0x19])
                    self.spi.xfer2([ADDR, Q, 0x30])
                if Channel_Phase==149.0625:
                    self.spi.xfer2([ADDR, I, 0x1A])
                    self.spi.xfer2([ADDR, Q, 0x2F])
                if Channel_Phase==151.875:
                    self.spi.xfer2([ADDR, I, 0x1B])
                    self.spi.xfer2([ADDR, Q, 0x2E])
                if Channel_Phase==154.6875:
                    self.spi.xfer2([ADDR, I, 0x1C])
                    self.spi.xfer2([ADDR, Q, 0x2D])
                if Channel_Phase==157.5:
                    self.spi.xfer2([ADDR, I, 0x1C])
                    self.spi.xfer2([ADDR, Q, 0x2B])
                if Channel_Phase==160.3125:
                    self.spi.xfer2([ADDR, I, 0x1D])
                    self.spi.xfer2([ADDR, Q, 0x2A])
                if Channel_Phase==163.125:
                    self.spi.xfer2([ADDR, I, 0X1E])
                    self.spi.xfer2([ADDR, Q, 0x28])
                if Channel_Phase==165.9375:
                    self.spi.xfer2([ADDR, I, 0x1E])
                    self.spi.xfer2([ADDR, Q, 0x27])
                if Channel_Phase==168.75:
                    self.spi.xfer2([ADDR, I, 0x1E])
                    self.spi.xfer2([ADDR, Q, 0x26])
                if Channel_Phase==171.5625:
                    self.spi.xfer2([ADDR, I, 0x1F])
                    self.spi.xfer2([ADDR, Q, 0x24])
                if Channel_Phase==174.375:
                    self.spi.xfer2([ADDR, I, 0x1F])
                    self.spi.xfer2([ADDR, Q, 0x23])
                if Channel_Phase==177.1875:
                    self.spi.xfer2([ADDR, I, 0x1F])
                    self.spi.xfer2([ADDR, Q, 0x21])
                    
            # Quadrant 3
                if Channel_Phase==180:
                    self.spi.xfer2([ADDR, I, 0x1F])
                    self.spi.xfer2([ADDR, Q, 0x20])
                if Channel_Phase==182.8125:
                    self.spi.xfer2([ADDR, I, 0x1F])
                    self.spi.xfer2([ADDR, Q, 0x20])
                if Channel_Phase==185.625:
                    self.spi.xfer2([ADDR, I, 0x1F])
                    self.spi.xfer2([ADDR, Q, 0x03])
                if Channel_Phase==188.4375:
                    self.spi.xfer2([ADDR, I, 0x1F])
                    self.spi.xfer2([ADDR, Q, 0x04])
                if Channel_Phase==191.25:
                    self.spi.xfer2([ADDR, I, 0x1F])
                    self.spi.xfer2([ADDR, Q, 0x06])
                if Channel_Phase==194.0625:
                    self.spi.xfer2([ADDR, I, 0x1E])
                    self.spi.xfer2([ADDR, Q, 0x07])
                if Channel_Phase==196.875:
                    self.spi.xfer2([ADDR, I, 0x1E])
                    self.spi.xfer2([ADDR, Q, 0x08])
                if Channel_Phase==199.6875:
                    self.spi.xfer2([ADDR, I, 0x1D])
                    self.spi.xfer2([ADDR, Q, 0x0A])
                if Channel_Phase==202.5:
                    self.spi.xfer2([ADDR, I, 0x1D])
                    self.spi.xfer2([ADDR, Q, 0x0B])
                if Channel_Phase==205.3125:
                    self.spi.xfer2([ADDR, I, 0x1C])
                    self.spi.xfer2([ADDR, Q, 0x0D])
                if Channel_Phase==208.125:
                    self.spi.xfer2([ADDR, I, 0x1C])
                    self.spi.xfer2([ADDR, Q, 0x0E])
                if Channel_Phase==210.9375:
                    self.spi.xfer2([ADDR, I, 0x1B])
                    self.spi.xfer2([ADDR, Q, 0x0F])
                if Channel_Phase==213.75:
                    self.spi.xfer2([ADDR, I, 0x1A])
                    self.spi.xfer2([ADDR, Q, 0x10])
                if Channel_Phase==216.5625:
                    self.spi.xfer2([ADDR, I, 0x19])
                    self.spi.xfer2([ADDR, Q, 0x11])
                if Channel_Phase==219.375:
                    self.spi.xfer2([ADDR, I, 0x18])
                    self.spi.xfer2([ADDR, Q, 0x13])
                if Channel_Phase==222.1875:
                    self.spi.xfer2([ADDR, I, 0x17])
                    self.spi.xfer2([ADDR, Q, 0x14])
                if Channel_Phase==225:
                    self.spi.xfer2([ADDR, I, 0x16])
                    self.spi.xfer2([ADDR, Q, 0x15])
                if Channel_Phase==227.8125:
                    self.spi.xfer2([ADDR, I, 0x15])
                    self.spi.xfer2([ADDR, Q, 0x16])
                if Channel_Phase==230.625:
                    self.spi.xfer2([ADDR, I, 0x14])
                    self.spi.xfer2([ADDR, Q, 0x17])
                if Channel_Phase==233.4375:
                    self.spi.xfer2([ADDR, I, 0x13])
                    self.spi.xfer2([ADDR, Q, 0x18])
                if Channel_Phase==236.25:
                    self.spi.xfer2([ADDR, I, 0x12])
                    self.spi.xfer2([ADDR, Q, 0x18])
                if Channel_Phase==239.0625:
                    self.spi.xfer2([ADDR, I, 0x10])
                    self.spi.xfer2([ADDR, Q, 0x19])
                if Channel_Phase==241.875:
                    self.spi.xfer2([ADDR, I, 0x0F])
                    self.spi.xfer2([ADDR, Q, 0x1A])
                if Channel_Phase==244.6875:
                    self.spi.xfer2([ADDR, I, 0x0E])
                    self.spi.xfer2([ADDR, Q, 0x1A])
                if Channel_Phase==247.5:
                    self.spi.xfer2([ADDR, I, 0x0C])
                    self.spi.xfer2([ADDR, Q, 0x1B])
                if Channel_Phase==250.3125:
                    self.spi.xfer2([ADDR, I, 0x0B])
                    self.spi.xfer2([ADDR, Q, 0x1C])
                if Channel_Phase==253.125:
                    self.spi.xfer2([ADDR, I, 0x0A])
                    self.spi.xfer2([ADDR, Q, 0x1C])
                if Channel_Phase==255.9375:
                    self.spi.xfer2([ADDR, I, 0x08])
                    self.spi.xfer2([ADDR, Q, 0x1C])
                if Channel_Phase==258.75:
                    self.spi.xfer2([ADDR, I, 0x07])
                    self.spi.xfer2([ADDR, Q, 0x1D])
                if Channel_Phase==261.5625:
                    self.spi.xfer2([ADDR, I, 0x05])
                    self.spi.xfer2([ADDR, Q, 0x1D])
                if Channel_Phase==264.375:
                    self.spi.xfer2([ADDR, I, 0x04])
                    self.spi.xfer2([ADDR, Q, 0x1D])
                if Channel_Phase==267.1875:
                    self.spi.xfer2([ADDR, I, 0x02])
                    self.spi.xfer2([ADDR, Q, 0x1D])
            
            # Quadrant 4
                if Channel_Phase==270:
                    self.spi.xfer2([ADDR, I, 0x01])
                    self.spi.xfer2([ADDR, Q, 0x1D])
                if Channel_Phase==272.8125:
                    self.spi.xfer2([ADDR, I, 0x21])
                    self.spi.xfer2([ADDR, Q, 0x1D])
                if Channel_Phase==275.625:
                    self.spi.xfer2([ADDR, I, 0x23])
                    self.spi.xfer2([ADDR, Q, 0x1D])
                if Channel_Phase==278.4375:
                    self.spi.xfer2([ADDR, I, 0x24])
                    self.spi.xfer2([ADDR, Q, 0x1D])
                if Channel_Phase==281.25:
                    self.spi.xfer2([ADDR, I, 0x26])
                    self.spi.xfer2([ADDR, Q, 0x1D])
                if Channel_Phase==284.0625:
                    self.spi.xfer2([ADDR, I, 0x27])
                    self.spi.xfer2([ADDR, Q, 0x1C])
                if Channel_Phase==286.875:
                    self.spi.xfer2([ADDR, I, 0x28])
                    self.spi.xfer2([ADDR, Q, 0x1C])
                if Channel_Phase==289.6875:
                    self.spi.xfer2([ADDR, I, 0x2A])
                    self.spi.xfer2([ADDR, Q, 0x1C])
                if Channel_Phase==292.5:
                    self.spi.xfer2([ADDR, I, 0x2B])
                    self.spi.xfer2([ADDR, Q, 0x1B])
                if Channel_Phase==295.3125:
                    self.spi.xfer2([ADDR, I, 0x2D])
                    self.spi.xfer2([ADDR, Q, 0x1A])
                if Channel_Phase==298.125:
                    self.spi.xfer2([ADDR, I, 0x2E])
                    self.spi.xfer2([ADDR, Q, 0x1A])
                if Channel_Phase==300.9375:
                    self.spi.xfer2([ADDR, I, 0x2F])
                    self.spi.xfer2([ADDR, Q, 0x19])
                if Channel_Phase==303.75:
                    self.spi.xfer2([ADDR, I, 0x31])
                    self.spi.xfer2([ADDR, Q, 0x18])
                if Channel_Phase==306.5625:
                    self.spi.xfer2([ADDR, I, 0x32])
                    self.spi.xfer2([ADDR, Q, 0x18])
                if Channel_Phase==309.375:
                    self.spi.xfer2([ADDR, I, 0x33])
                    self.spi.xfer2([ADDR, Q, 0x17])
                if Channel_Phase==312.1875:
                    self.spi.xfer2([ADDR, I, 0x34])
                    self.spi.xfer2([ADDR, Q, 0x16])
                if Channel_Phase==315:
                    self.spi.xfer2([ADDR, I, 0x36])
                    self.spi.xfer2([ADDR, Q, 0x15])
                if Channel_Phase==317.8125:
                    self.spi.xfer2([ADDR, I, 0x37])
                    self.spi.xfer2([ADDR, Q, 0x14])
                if Channel_Phase==320.625:
                    self.spi.xfer2([ADDR, I, 0x38])
                    self.spi.xfer2([ADDR, Q, 0x13])
                if Channel_Phase==323.4375:
                    self.spi.xfer2([ADDR, I, 0x39])
                    self.spi.xfer2([ADDR, Q, 0x11])
                if Channel_Phase==326.25:
                    self.spi.xfer2([ADDR, I, 0x39])
                    self.spi.xfer2([ADDR, Q, 0x10])
                if Channel_Phase==329.0625:
                    self.spi.xfer2([ADDR, I, 0x3A])
                    self.spi.xfer2([ADDR, Q, 0x0F])
                if Channel_Phase==331.875:
                    self.spi.xfer2([ADDR, I, 0x3B])
                    self.spi.xfer2([ADDR, Q, 0x0E])
                if Channel_Phase==334.6875:
                    self.spi.xfer2([ADDR, I, 0x3C])
                    self.spi.xfer2([ADDR, Q, 0x0D])
                if Channel_Phase==337.5:
                    self.spi.xfer2([ADDR, I, 0x3C])
                    self.spi.xfer2([ADDR, Q, 0x0B])
                if Channel_Phase==340.3125:
                    self.spi.xfer2([ADDR, I, 0x3D])
                    self.spi.xfer2([ADDR, Q, 0x0A])
                if Channel_Phase==343.125:
                    self.spi.xfer2([ADDR, I, 0x3E])
                    self.spi.xfer2([ADDR, Q, 0x08])
                if Channel_Phase==345.9375:
                    self.spi.xfer2([ADDR, I, 0x3E])
                    self.spi.xfer2([ADDR, Q, 0x07])
                if Channel_Phase==348.75:
                    self.spi.xfer2([ADDR, I, 0x3E])
                    self.spi.xfer2([ADDR, Q, 0x06])
                if Channel_Phase==351.5625:
                    self.spi.xfer2([ADDR, I, 0x3F])
                    self.spi.xfer2([ADDR, Q, 0x04])
                if Channel_Phase==354.375:
                    self.spi.xfer2([ADDR, I, 0x3F])
                    self.spi.xfer2([ADDR, Q, 0x03])
                if Channel_Phase==357.1875:
                    self.spi.xfer2([ADDR, I, 0x3F])
                    self.spi.xfer2([ADDR, Q, 0x01])
                    
            self.spi.xfer2([ADDR1, 0x28, 0x01])  # Loads Rx vectors from SPI.  0x08 is all ADAR1000 devices


            total=0
            for count in range (0,self.Averages):
                if self.adi_install==True:
                    data=self.sdr.rx()          #read a buffer of data from Pluto using pyadi-iio library (adi.py)
                else:
                    self.rxbuf.refill()     # this is for iio.py bindings
                    read_data = self.rxbuf.read()   #this is for iio.py bindings
                    data = np.frombuffer(read_data,dtype=np.int16)
                N = len(data)               #number of samples
                win = np.hamming(N)
                y = data * win
                sp = np.absolute(np.fft.fft(y))
                sp = sp[1:-1]
                sp = np.fft.fftshift(sp)
                s_mag = np.abs(sp) * 2 / np.sum(win)
                s_dbfs = 20*np.log10(s_mag/(2**12))
                total=total+max(s_dbfs)   # sum up all the loops, then we'll average
            PeakValue=total/self.Averages
            
            if PeakValue>max_signal:    #take the largest value, so that we know where to point the compass
                max_signal=PeakValue
                max_angle=SteerAngle
                
            output_items[0][PhaseStepNumber]=((-1)*SteerAngle+90 + (1j * PeakValue))  # output this as a complex number so we can do an x-y plot with the constellation graph
            PhaseStepNumber=PhaseStepNumber+1    # increment the phase delta and start this whole again.  This will repeat 140 times

        output_items[0]=output_items[0][0:PhaseStepNumber]
        output_items[1][:] = max_angle * (-1)+90
            
        return len(output_items[0])



