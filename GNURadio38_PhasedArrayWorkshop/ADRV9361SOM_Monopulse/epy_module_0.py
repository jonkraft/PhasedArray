# this module will be imported in the into your flowgraph
# You can learn more about SPI and Rasp Pi at https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial/all#spi-on-pi

import time
import spidev

# We only have SPI bus 0 available to us on the Pi
bus = 0

#Device is the chip select pin. Set to 0 or 1, depending on the connections
device = 0

# Enable SPI
spi = spidev.SpiDev()

# Open a connection to a specific bus and device (chip select pin)
spi.open(bus, device)

# Set SPI speed and mode
spi.max_speed_hz = 500000
spi.mode = 0

# Rasp Pi Broadcom chip can only do 8 bit SPI writes.
# So the 24 bit SPI writes of the ADAR1000 need to be broken
# into 3 chunks.  Use the xfer2 command to keep CS low, until all 4 are there.

ADDR1 = 0x20
ADDR2 = 0x40

beamformers = [ADDR1, ADDR2]

for ADDR in beamformers:
    # Initialize the ADAR1000
    spi.xfer2([ADDR, 0x00, 0x81])  # reset the device
    spi.xfer2([ADDR, 0x00, 0x18])  # Sets SDO  pin to active (4 wire SPI)
    spi.xfer2([ADDR+0x04, 0x00, 0x55])  # Trims LDO to 1.8V
    spi.xfer2([ADDR, 0x38, 0x60])  # Bypasses beam and bias RAM (use SPI for gain/phase)
    spi.xfer2([ADDR, 0x2E, 0x7F])  # Enables all 4 Rx channels, LNA, VGA, and Vector Mod
    spi.xfer2([ADDR, 0x34, 0x08])  # Sets LNA bias to middle of its range
    spi.xfer2([ADDR, 0x35, 0x16])  # Sets VGA bias to [0010] and vector mod bias to [110]
    spi.xfer2([ADDR, 0x31, 0xB0])  # Enables the whole Rx and sets the ADTR1107 switch high (Rx mode)
    time.sleep(0.1)

    # Write registers to set Rx1-4 to 45 deg and Max Gain
    spi.xfer2([ADDR, 0x10, 0xFF])  # Sets Rx1 to max gain
    spi.xfer2([ADDR, 0x14, 0x36])  # Sets Rx1 I vector to positive and [10110]
    spi.xfer2([ADDR, 0x15, 0x36])  # Sets Rx1 Q vector to positive and [10110]
    spi.xfer2([ADDR, 0x11, 0xFF])  # Sets Rx2 to max gain
    spi.xfer2([ADDR, 0x16, 0x36])  # Sets Rx2 I vector to positive and [10110]
    spi.xfer2([ADDR, 0x17, 0x36])  # Sets Rx2 Q vector to positive and [10110]
    spi.xfer2([ADDR, 0x12, 0xFF])  # Sets Rx3 to max gain
    spi.xfer2([ADDR, 0x18, 0x36])  # Sets Rx3 I vector to positive and [10110]
    spi.xfer2([ADDR, 0x19, 0x36])  # Sets Rx3 Q vector to positive and [10110]
    spi.xfer2([ADDR, 0x13, 0xFF])  # Sets Rx4 to max gain
    spi.xfer2([ADDR, 0x1A, 0x36])  # Sets Rx4 I vector to positive and [10110]
    spi.xfer2([ADDR, 0x1B, 0x36])  # Sets Rx4 Q vector to positive and [10110]
      
    spi.xfer2([ADDR, 0x28, 0x01])  # Loads Rx vectors from SPI.
    time.sleep(0.1)

# Power down the ADAR1000
#spi.xfer2([ADDR, 0x00, 0x81])  # reset the device
#spi.xfer2([ADDR, 0x00, 0x18])  # Sets SDO  pin to active (4 wire SPI)
#spi.xfer2([ADDR+0x04, 0x00, 0x55])  # Trims LDO to 1.8V


