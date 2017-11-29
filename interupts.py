#!/usr/bin/python
#Shane Miller (Not original code)
# Script written by Alex Eames. Http://RasPi.tv. Original comments retained.
# Slight variations made by Justin Limbach 
#Stolen from Justin Limbach (I changed some of the comments)
    #updated LCD messages 

import RPi.GPIO as GPIO
import time
# Displaying to LCD 
import Adafruit_CharLCD as LCD
lcd = LCD.Adafruit_CharLCDPlate()
GPIO.setmode(GPIO.BCM)

# Pins 23 & 24 are set up as inputs. Justin Limbach) modified the original
# Waits for falling edge.
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
time_stamp = time.time()

# defines the threaded callback function
# will run in another thread when our event is detected
def my_callback(channel):
    lcd.clear()
    lcd.message('Port 24 \n falls')

    # Omitted extra print lines here, because why not. 

raw_input(lcd.message('  As you want, \n   Shane\n>'))
# when port 24 has falling edge, my_callback happens

GPIO.add_event_detect(24, GPIO.FALLING, callback=my_callback, bouncetime = 200)

# Changed the text to talk to me 
try:
    lcd.clear()
    lcd.message('   Pointing at \n    Port 23')
    GPIO.wait_for_edge(23, GPIO.FALLING)
    lcd.clear()
    lcd.message('   edge \n   has falls.')

except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()
