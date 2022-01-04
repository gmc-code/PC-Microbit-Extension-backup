# 4tronix BitBotXL forwards
from microbit import *

def bbxl_forwards(speed=200):
    pin16.write_analog(speed)    # left forward
    pin8.write_digital(0)    # left backward
    pin14.write_analog(speed)    # right forward
    pin12.write_digital(0)    # right backward

bbxl_forwards(200)

