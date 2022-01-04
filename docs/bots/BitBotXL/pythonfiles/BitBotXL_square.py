# 4tronix BitBotXL square
from microbit import *

LMF = pin16
LMB = pin8
RMF = pin14
RMB = pin12

def bbxl_forward(speed=200):
    LMF.write_analog(speed)    # left forward
    LMB.write_digital(0)    # left backward
    RMF.write_analog(speed)    # right forward
    RMB.write_digital(0)    # right backward

def bbxl_spinleft(speed=200):
    LMF.write_analog(speed)    # left forward
    LMB.write_digital(0)    # left backward
    RMF.write_digital(0)     # right forward
    RMB.write_analog(speed)    # right backward

while True:
  for i in range(4):
    bbxl_forward(200)
    sleep(4000)
    bbxl_spinleft(200)
    sleep(1000)
