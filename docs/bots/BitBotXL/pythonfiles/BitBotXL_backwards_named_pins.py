# 4tronix BitBotXL backwards
from microbit import *

LMF = pin16
LMB = pin8
RMF = pin14
RMB = pin12

def bbxl_backwards(speed=200):
    LMF.write_digital(0)  # left forward
    LMB.write_analog(speed)  # left backward
    RMF.write_digital(0)  # right forward
    RMB.write_analog(speed)  # right backward

bbxl_backwards(200)
