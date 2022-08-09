'''
Blink LED - Simple Example
Author: João Pedro Carvalho Moreira
E-mail: mcjpedro@gmail.com
Núcleo de Neurociências - NNC
Universidade Federal de Minas Gerais - UFMG

  This code makes an LED to blink when connected to the Raspberry Pi's GPIO
'''

import RPi.GPIO as GPIO        # Impórt the RPi.GPIO library
import time                    # Import the time library

GPIO.setmode(GPIO.BOARD)       # Set the numbering of the pins (BOARD: physical, BCM: schematic)
GPIO.setwarnings(False)        # Ocult the warnings 
GPIO.setup(12, GPIO.OUT)       # Set the pin (12) and the mode (OUT or IN)
while(1):                      # While the code runs
    print("LED on")            # Display "LED on"
    GPIO.output(12,GPIO.HIGH)  # Set the pin to high value 
    time.sleep(0.1)            # Freeze the code 
    print("LED off")           # Display "LED off"
    GPIO.output(12,GPIO.LOW)   # Set the pin to low value
    time.sleep(0.1)            # Freeze the code
    