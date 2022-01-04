# BitBotXL LEDs # R-G-B-R gradients
from microbit import *
import neopixel

PIN_NUM = pin13
NUM_PIXELS = 12
np = neopixel.NeoPixel(PIN_NUM, NUM_PIXELS)

def bb_left_lights(brt = 10):
    np[0] = (brt, 0, 0)
    np[1] = (brt, brt, 0)
    np[2] = (0, brt, 0)
    np[3] = (0, brt, brt)
    np[4] = (0, 0, brt)
    np[5] = (brt, brt, brt)
    np.show()

def bb_right_lights(brt = 10):
    np[6] = (brt, 0, 0)
    np[7] = (brt, brt, 0)
    np[8] = (0, brt, 0)
    np[9] = (0, brt, brt)
    np[10] = (0, 0, brt)
    np[11] = (brt, brt, brt)
    np.show()

def bb_lights_off():
    bb_left_lights(brt = 0)
    bb_right_lights(brt = 0)

for n in range(2):
    for i in range(1,10,1):
        bb_left_lights(brt = i)
        bb_right_lights(brt = 10 - i)
        sleep(10)
    for i in range(1,10,1):
        bb_left_lights(brt = 10 - i)
        bb_right_lights(brt = i)
        sleep(10)
    bb_lights_off()
    sleep(100)

for n in range(2):
    for i in range(1,10,1):
        bb_left_lights(brt = i)
        bb_right_lights(brt = i)
        sleep(10)
    for i in range(1,10,1):
        bb_left_lights(brt = 10 - i)
        bb_right_lights(brt = 10 - i)
        sleep(10)
    bb_lights_off()
    sleep(100)
