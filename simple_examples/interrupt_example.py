'''
Threaded Callback Interrupt - Simple Example
Author: João Pedro Carvalho Moreira
E-mail: mcjpedro@gmail.com
Núcleo de Neurociências - NNC
Universidade Federal de Minas Gerais - UFMG
 
The Interrupt_Example.py code is a simple example of chained interrupt callback functions. It is possible to control by buttons (switches) the frequency of an LED
inserted in a circuit with a resistor (470 Ohms is enough). The button 1 increase the frequency, the button 2 decrease the frequency and the button 3 reset the frequency
to 5Hz.
'''

import RPi.GPIO as GPIO                         # import RPi.GPIO library as GPIO variable
import time                                     # Import time library

GPIO.setmode(GPIO.BOARD)                        # Set the pins map
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set the pin 13 trigger on falling edge  
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set the pin 13 trigger on falling edge
GPIO.setup(11, GPIO.OUT)                             # Set the pin 18 with output
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set the pin 13 trigger on rising edge

global LED_frequency                                 # Set global variable
LED_frequency = 5                                    # Set the first value to the account
 
def my_callback1(channel):                                # Callback function - button 1
    global LED_frequency                                  # Set global variable
    if LED_frequency + 1 == 50:                           # If the time reaches a negative value
        print("The maximum frequency has been reached")   # It's impossible, display a warning message
        return                                            # Return the function
    else:
        print("You press the button 2 - Decreases")       # Display the action
        LED_frequency = LED_frequency + 1                 # Set the account
        print("LED frequency = ", LED_frequency, "Hz")    # Display the result
    
def my_callback2(channel):                                # Callback function - button 2
    global LED_frequency                                  # Set global variable
    if LED_frequency - 1 == 0:                            # If the time reaches a negative value
        print("The minimum frequency has been reached")   # It's impossible, display a warning message
        return                                            # Return the function
    else:                                                 # If it's still possible increase the frequency
        print("You press the button 1 - Increases")       # Display the action
        LED_frequency = LED_frequency - 1                 # Set the account
        print("LED frequency = ", LED_frequency, "Hz")    # Display the result          
    
def my_callback3(channel):                                # Callback function - button 3
    global LED_frequency                                  # Set global variable
    print("You press the button 3 - Reset")               # Display the action
    LED_frequency = 5                                     # Set the account
    print("LED frequency = ", LED_frequency, "Hz")        # Display the result
  
GPIO.add_event_detect(18, GPIO.FALLING, callback=my_callback1, bouncetime=300)  # Callback command button 1
  
GPIO.add_event_detect(16, GPIO.FALLING, callback=my_callback2, bouncetime=300)  # Callback command button 2

GPIO.add_event_detect(13, GPIO.RISING, callback=my_callback3, bouncetime=300)   # Callback command button 3 

try:
    print("This is a simple LED frequency controller, press:")
    print("  - Button 1 to increase")
    print("  - Button 2 to decrease")
    print("  - Button 3 to reset")
    while(1):                        # While the code runs
        GPIO.output(11,GPIO.HIGH)    # Set the pin to high value 
        time.sleep(1/LED_frequency)  # Freeze the code 
        GPIO.output(11,GPIO.LOW)     # Set the pin to low value
        time.sleep(1/LED_frequency)  # Freeze the code

except KeyboardInterrupt:  
    GPIO.cleanup()                 # clean up GPIO on CTRL+C exit  

GPIO.cleanup()                     # clean up GPIO on normal exit 
