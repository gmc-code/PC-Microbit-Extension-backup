# 4tronix BitBotXL spin
from microbit import *

LMF = pin16
LMB = pin8
RMF = pin14
RMB = pin12

def bbxl_spinright(speed=200):
    LMF.write_analog(speed)    # left forward
    LMB.write_digital(0)    # left backward
    RMF.write_digital(0)     # right forward
    RMB.write_analog(speed)    # right backward

def bbxl_spinleft(speed=200):
    LMF.write_digital(0)    # left forward
    LMB.write_analog(speed)    # left backward
    RMF.write_analog(speed)     # right forward
    RMB.write_digital(0)    # right backward

while True:
    for i in range(200,1000,100):
        bbxl_spinright(i)
        sleep(1000)
    for i in range(200,1000,100):
        bbxl_spinleft(i,)
        sleep(1000)
