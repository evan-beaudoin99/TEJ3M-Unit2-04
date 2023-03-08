# Created by: Evan Beaudoin
# Created on: March 2023
#
#  Changes the colors of an RGB LED.

import time
import board
from digitalio import DigitalInOut, Direction


RED_LED = DigitalInOut(board.GP8)
GREEN_LED = DigitalInOut(board.GP10)
BLUE_LED= DigitalInOut(board.GP12)

RED_BLUE.direction = Direction.OUTPUT
GREEN_LED.direction = Direction.OUTPUT
BLUE_LED.direction = Direction.OUTPUT


def set_color(red_value, green_value, blue_value):
    RED_VALUE.value = red_value
    GREEN_VALUE.value = green_value
    BLUE_VALUE.value = blue_value

while True:
    
    set_color(True, False, False) # Red Color
    time.sleep(1)
    set_color(False, True, False) # Green Color
    time.sleep(1)
    set_color(False, False, True) # Blue Color
    time.sleep(1)
    set_color(True, True, False) # Yellow Color
    time.sleep(1)
    set_color(True, False, True) # Purple Color
    time.sleep(1)
    set_color(True, True, True) # White Color
    time.sleep(1)
   
