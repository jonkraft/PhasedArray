"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import time
import spidev
import RPi.GPIO as GPIO

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Set ADF5356 Freq Using QT GUI variables"""

    def __init__(self, Signal=10.5):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='ADF5356_Freq',   # this name will show up in GRC
            in_sig=[],             # normally this is [np.complex64] or something.  But we don't need any inputs for this block.
            out_sig=[np.complex64]      # We really don't need any outputs, but it complains if I leave both inputs and outputs as null.
        )
        self.Signal = Signal
        self.Change = 1
        self.current_freq = 0

        # It's best to toggle ADF5356 enable prior to startup.  Just to reset everything.
        GPIO.setwarnings(False)
        GPIO.PUD_UP
        GPIO.setmode(GPIO.BOARD)   # use the pin numbers (1-40) on the Rasp Pi header
        GPIO.setup(11, GPIO.OUT)   # set pin 11 (which BCM calls "GPIO 17") to an output
        GPIO.output(11, GPIO.LOW)
        time.sleep(1)
        GPIO.output(11, GPIO.HIGH)
        time.sleep(1)
        
        bus = 0      # We only have SPI bus 0 available to us on the Pi, so this is always 0
        device = 1   # Device is the chip select pin. "0" is being used by the ADAR1000, so this need to be "1" for the ADF5356's chip select
        self.spi = spidev.SpiDev()    # Enable SPI
        self.spi.open(bus, device)    # Open a connection to a specific bus and device (chip select pin)
        self.spi.max_speed_hz = 500000   # Set SPI speed
        self.spi.mode = 0                # Set SPI mode (ADF5356 is mode 0)
        
    def work(self, input_items, output_items):
        #output_items[0][:] = input_items[0] * 1
        time.sleep(2)   # we only need to check this sporadically.  So this does the check every 2 sec (instead of checking it repeatedly as fast possible!)
        def ADF5356_init():   # this function initializes the ADF5356.  It's overkill to call it every time we change freq, but that makes my setup more robust.
            self.spi.xfer2([0x00, 0x00, 0x00, 0x0D])   # R13 0x0D
            self.spi.xfer2([0x00, 0x00, 0x15, 0xFC])   # R12 0x15FC
            self.spi.xfer2([0x00, 0x61, 0x20, 0x0B])   # R11 0x61200B
            self.spi.xfer2([0x00, 0xC0, 0x26, 0xBA])   # R10 0xC026BA
            self.spi.xfer2([0x27, 0x19, 0xFC, 0xC9])   # R9  0x2719FCC9
            self.spi.xfer2([0x15, 0x59, 0x65, 0x68])   # R8  0x15596568
            self.spi.xfer2([0x06, 0x00, 0x00, 0xE7])   # R7  0x60000E7
            self.spi.xfer2([0x35, 0x03, 0x00, 0x06])   # R6  0x35030006
            self.spi.xfer2([0x00, 0x80, 0x00, 0x25])   # R5  0x800025
            self.spi.xfer2([0x32, 0x00, 0x8B, 0x84])   # R4  0x32008B84
            self.spi.xfer2([0x00, 0x00, 0x00, 0x03])   # R3  0x3
            print("ADF5356_init function")
            time.sleep(1)
            
        if self.current_freq != self.Signal:   # if the freq has changed then redo the init function and program the new freq
            self.Change = 1
        else:
            self.Change = 0

        if self.Change == 1:
            self.current_freq = self.Signal            
            ADF5356_init()
            for i in range(2):   # write the ADF5356 registers twice, just for error redundancy
                # Write registers to set freq to 9.5 GHz
                if self.Signal==9.5:
                    self.spi.xfer2([0x00, 0x08, 0x00, 0x32]) # R2     0x80032
                    self.spi.xfer2([0x04, 0xFA, 0xAA, 0xA1]) # R1     0x4FAAAA1
                    time.sleep(0.001)   # wait for ADC to settle
                    self.spi.xfer2([0x00, 0x20, 0x04, 0xD0]) # R0     0x2004D0
                    print("ADF5356 is set to 9.5 GHz")

                # Write registers to set freq to 10 GHz
                if self.Signal==10:
                    self.spi.xfer2([0x00, 0x04, 0x00, 0x32]) # R2  0x40032
                    self.spi.xfer2([0x06, 0x15, 0x55, 0x51]) # R1  0x6155551
                    time.sleep(0.001)   # wait for ADC to settle
                    self.spi.xfer2([0x00, 0x30, 0x05, 0x10]) # R0  0x300510
                    print("ADF5356 is set to 10 GHz")

                # Write registers to set freq to 10.5 GHz
                if self.Signal==10.5:
                    self.spi.xfer2([0x00, 0x00, 0x00, 0x12]) # R2     0x12
                    self.spi.xfer2([0x07, 0x30, 0x00, 0x01]) # R1     0x7300001
                    time.sleep(0.001)   # wait for ADC to settle
                    self.spi.xfer2([0x00, 0x20, 0x05, 0x50]) # R0     0x200550
                    print("ADF5356 is set to 10.5 GHz")

                # Write registers to set freq to 11 GHz
                if self.Signal==11:
                    self.spi.xfer2([0x00, 0x08, 0x00, 0x32]) # R2     0x80032
                    self.spi.xfer2([0x08, 0x4A, 0xAA, 0xA1]) # R1     0x84AAAA1
                    time.sleep(0.001)   # wait for ADC to settle
                    self.spi.xfer2([0x00, 0x20, 0x05, 0x90]) # R0     0x200590
                    print("ADF5356 is set to 11 GHz")

                # Power down the ADF5356
                if self.Signal==11.5:
                    self.spi.xfer2([0x00, 0x00, 0x00, 0x44])
                    print("ADF5356 is shutdown")
                    time.sleep(0.5)
                    
        return len(output_items[0])






