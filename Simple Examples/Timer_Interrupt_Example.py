import NNClib
import threading
import RPi.GPIO as GPIO                         # Import RPi.GPIO library as GPIO variable

all_configurations = {"chip"              : "RHD2132",
                      "sampling_frequency": 1,
                      "highpass_frequency": 0,
                      "lowpass_frequency" : 20000,
                      "timed_record"      : "yes",
                      "time_day"          : 0,
                      "time_hour"         : 0,
                      "time_min"          : 0,
                      "time_sec"          : 0,
                      "auto_save"         : "no",
                      "channels"          : [],
                      "number_channels"   : 32}

NNClib.say_hello()

# GPIO.setmode(GPIO.BOARD)                            # Set the pins map
# GPIO.setwarnings(False)
# GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # Set the pin 18 trigger on falling edge 

# mosi = [int('0xAA',16), int('0xAA',16)]             # Set the message (to send 16 bits, make a list with 2 values)

# def callback_function_RHD():
#     miso = spi.xfer2(mosi)                          # Make the SPI transfer, send a message and get another one
#     return miso

# threading.Timer(5, callback_function_RHD).start()                                           # Timer interrupt to record (RHD)   


















