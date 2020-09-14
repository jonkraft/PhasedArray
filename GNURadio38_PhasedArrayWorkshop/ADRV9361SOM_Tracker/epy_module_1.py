# SPI commands to set the ADF4371 output frequency to 9.5 GHz

'''
Useful resources:
    Introduction to Phased Array Antennas: https://www.analog.com/en/analog-dialogue/articles/phased-array-antenna-patterns-part1.html#
    Full workshop build instructions at www.github.com/jonkraft/phasedarray
    Analog Devices Python Interfaces:  https://analogdevicesinc.github.io/pyadi-iio/
    Python examples:  https://github.com/analogdevicesinc/pyadi-iio/tree/ensm-example/examples
    GNU Radio and IIO Devices:  https://wiki.analog.com/resources/tools-software/linux-software/gnuradio
    ADI Kuiper Linux for Raspberry Pi:  https://wiki.analog.com/resources/tools-software/linux-software/gnuradio
'''

# Copyright (C) 2019 Analog Devices, Inc.
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#     - Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     - Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in
#       the documentation and/or other materials provided with the
#       distribution.
#     - Neither the name of Analog Devices, Inc. nor the names of its
#       contributors may be used to endorse or promote products derived
#       from this software without specific prior written permission.
#     - The use of this software may or may not infringe the patent rights
#       of one or more patent holders.  This license does not release you
#       from the requirement that you obtain separate licenses from these
#       patent holders to use this software.
#     - Use of the software either in source or binary form, must be run
#       on or directly connected to an Analog Devices Inc. component.
#
# THIS SOFTWARE IS PROVIDED BY ANALOG DEVICES "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED.
#
# IN NO EVENT SHALL ANALOG DEVICES BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, INTELLECTUAL PROPERTY
# RIGHTS, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
# THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# You can learn more about SPI and Rasp Pi at https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial/all#spi-on-pi

import time
import spidev

# We only have SPI bus 0 available to us on the Pi
bus = 0

#Device is the chip select pin. Set to 0 or 1, depending on the connections
device = 1

# Enable SPI
spi = spidev.SpiDev()

# Open a connection to a specific bus and device (chip select pin)
spi.open(bus, device)

# Set SPI speed and mode
spi.max_speed_hz = 500000
spi.mode = 0

# Rasp Pi Broadcom chip can only do 8 bit SPI writes.
# So the 24 bit SPI writes of the ADF4371 need to be broken
# into 3 chunks.  Use the xfer2 command to keep CS low, until all 4 are there.

'''RF16 port outputs 9.5GHz'''
spi.xfer2([0x00, 0x00, 0x18])  # 
spi.xfer2([0x00, 0x01, 0x00])  # 
spi.xfer2([0x00, 0x20, 0x14])  # 
spi.xfer2([0x00, 0x00, 0x18])  # 
spi.xfer2([0x00, 0x01, 0x00])  # 
spi.xfer2([0x00, 0x04, 0x00])  # 
spi.xfer2([0x00, 0x05, 0x00])  # 
spi.xfer2([0x00, 0x11, 0x00])  #

spi.xfer2([0x00, 0x12, 0x40])  # 
spi.xfer2([0x00, 0x14, 0x00])  # 
spi.xfer2([0x00, 0x15, 0x00])  # 
spi.xfer2([0x00, 0x16, 0x00])  # 
spi.xfer2([0x00, 0x17, 0x01])  # 
spi.xfer2([0x00, 0x18, 0x00])  # 
spi.xfer2([0x00, 0x19, 0x01])  # 
spi.xfer2([0x00, 0x1A, 0x00])  # 
spi.xfer2([0x00, 0x1B, 0x00])  # 
spi.xfer2([0x00, 0x1C, 0x00])  # 
spi.xfer2([0x00, 0x1D, 0x00])  # 
spi.xfer2([0x00, 0x1E, 0x48])  #

spi.xfer2([0x00, 0x1F, 0x01])  # 
spi.xfer2([0x00, 0x20, 0x14])  # 
spi.xfer2([0x00, 0x21, 0x00])  # 
spi.xfer2([0x00, 0x22, 0x00])  # 
spi.xfer2([0x00, 0x23, 0x00])  # 
spi.xfer2([0x00, 0x24, 0x80])  # 
spi.xfer2([0x00, 0x25, 0x0B])  # 
spi.xfer2([0x00, 0x26, 0x22])  # 
spi.xfer2([0x00, 0x27, 0xCD])  # 
spi.xfer2([0x00, 0x28, 0x83])  # 
spi.xfer2([0x00, 0x2A, 0x00])  # 
spi.xfer2([0x00, 0x2B, 0x00])  #

spi.xfer2([0x00, 0x2C, 0x44])  # 
spi.xfer2([0x00, 0x2D, 0x11])  # 
spi.xfer2([0x00, 0x2E, 0x12])  # 
spi.xfer2([0x00, 0x2F, 0x94])  # 
spi.xfer2([0x00, 0x30, 0x2A])  # 
spi.xfer2([0x00, 0x31, 0x02])  # 
spi.xfer2([0x00, 0x32, 0x04])  # 
spi.xfer2([0x00, 0x33, 0x22])  # 
spi.xfer2([0x00, 0x34, 0x85])  # 
spi.xfer2([0x00, 0x35, 0xFA])  # 
spi.xfer2([0x00, 0x36, 0x30])  #

spi.xfer2([0x00, 0x37, 0x00])  # 
spi.xfer2([0x00, 0x38, 0x00])  # 
spi.xfer2([0x00, 0x39, 0x07])  # 
spi.xfer2([0x00, 0x3A, 0x55])  # 
spi.xfer2([0x00, 0x3D, 0x00])  # 
spi.xfer2([0x00, 0x3E, 0x0C])  # 
spi.xfer2([0x00, 0x3F, 0x80])  # 
spi.xfer2([0x00, 0x40, 0x50])  # 
spi.xfer2([0x00, 0x41, 0x28])  # 
spi.xfer2([0x00, 0x42, 0x00])  # 
spi.xfer2([0x00, 0x43, 0x00])  #

spi.xfer2([0x00, 0x44, 0x00])  # 
spi.xfer2([0x00, 0x45, 0x00])  # 
spi.xfer2([0x00, 0x46, 0x00])  # 
spi.xfer2([0x00, 0x47, 0xC0])  # 
spi.xfer2([0x00, 0x52, 0xF4])  # 
spi.xfer2([0x00, 0x6C, 0x00])  # 
spi.xfer2([0x00, 0x70, 0xE3])  # 
spi.xfer2([0x00, 0x71, 0x60])  # 
spi.xfer2([0x00, 0x72, 0x32])  # 
spi.xfer2([0x00, 0x73, 0x00])  # 
spi.xfer2([0x00, 0x10, 0x2F])  # 

time.sleep(0.1)



