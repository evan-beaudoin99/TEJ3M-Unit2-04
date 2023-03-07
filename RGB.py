# Created by: Evan Beaudoin
# Created on: March 2023
#
#  Changes the colors of an RGB LED.

import time
import board
from digitalio import DigitalInOut, Direction


red_led = DigitalInOut(board.GP8)
red_led.direction = Direction.OUTPUT
green_led = DigitalInOut(board.GP10)
green_led.direction = Direction.OUTPUT
blue_led = DigitalInOut(board.GP12)
blue_led.direction = Direction.OUTPUT


def setColor(redValue, greenValue, blueValue):
    red_led.value = redValue
    green_led.value = greenValue
    blue_led.value = blueValue

while True:
    
    setColor(True, False, False) # Red Color
    time.sleep(1)
    setColor(False, True, False) # Green Color
    time.sleep(1)
    setColor(False, False, True) # Blue Color
    time.sleep(1)
    setColor(True, True, False) # Yellow Color
    time.sleep(1)
    setColor(True, False, True) # Purple Color
    time.sleep(1)
    setColor(True, True, True) # White Color
    time.sleep(1)
   
