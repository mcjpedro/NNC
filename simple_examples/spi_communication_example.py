'''
SPI Communication - Simple Example
Author: João Pedro Carvalho Moreira
E-mail: mcjpedro@gmail.com
Núcleo de Neurociências - NNC
Universidade Federal de Minas Gerais - UFMG

This code makes a simple SPI communication between the raspberry Pi and any device
connected to it. (An interesting way to test communication is to short circuit MOSI
and MISO).
'''

import spidev                # Import the SpiDev Library
import time                  # Import the time Library

bus = 0                      # Set the communication bus (Raspberry Pi pin SPI0 and SPI1)
device = 0                   # Set the communication device (Chip select)
spi = spidev.SpiDev()        # Initialize the SPI communication variable
spi.open(bus, device)        # Open the SPI communication
spi.lsbfirst = False         # Set MSB (On Raspberry Pi has no native LSB)
spi.bits_per_word = 8        # Set the number of bits per word (Raspberry Pi only accepts 8 bits per word)
spi.max_speed_hz = 8000      # Set the clock frequency (The maximum frequency on Raspberry Pi is 32MHz)
spi.mode = 2                 # Set the SPI mode (polarity and phase)
msg = [int('0xAA',16), int('0xAA',16),]   # Set the message (to send 16 bits, make a list with 2 values)
#print(msg)                  # Display the message to be sent
while(1):
    result = spi.xfer2(msg)  # Send the message and receive the output
    time.sleep(0.0005)       # Freeze
#print(result)               # Display the result 
