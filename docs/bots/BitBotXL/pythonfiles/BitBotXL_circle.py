# 4tronix BitBotXL cirle
from microbit import *

LMF = pin16
LMB = pin8
RMF = pin14
RMB = pin12

def bbxl_circle(lspeed=400, rspeed=200):
    LMF.write_analog(lspeed)    # left forward
    LMB.write_digital(0)    # left backward
    RMF.write_analog(rspeed)     # right forward
    RMB.write_digital(0)    # right backward

def bbxl_stop():
    LMF.write_analog(0)    # left forward
    LMB.write_digital(0)    # left backward
    RMF.write_analog(0)    # right forward
    RMB.write_digital(0)    # right backward

bbxl_circle(lspeed=400, rspeed=200)
sleep(10000)
bbxl_stop(2000)
