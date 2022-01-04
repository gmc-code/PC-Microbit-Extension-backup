# 4tronix BitBotXL backwards
from microbit import *

def bbxl_backwards(speed=200):
    pin16.write_digital(0)    # left forward
    pin8.write_analog(speed)    # left backward
    pin14.write_digital(0)    # right forward
    pin12.write_analog(speed)    # right backward

bbxl_backwards(200)
