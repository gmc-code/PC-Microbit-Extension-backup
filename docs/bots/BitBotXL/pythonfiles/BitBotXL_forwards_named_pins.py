# 4tronix BitBotXL forwards
from microbit import *

LMF = pin16
LMB = pin8
RMF = pin14
RMB = pin12

def bbxl_forwards(mb_speed=200):
    LMF.write_analog(mb_speed)    # left forward
    LMB.write_digital(0)    # left backward
    RMF.write_analog(mb_speed)    # right forward
    RMB.write_digital(0)    # right backward


bbxl_forwards(200)
