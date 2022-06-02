from microbit import *
import neopixel
import utime


DISTANCE_SENSOR_PIN = pin15

class bitBotXL:
    def __init__(self):
        pass

    def forward(self, speed):
        if (speed > 1023) or (speed < 1):
            print("Error, speed must be a number 1-1023")
            display.scroll("Speed must be a number 1-1023")
        else:
            pin16.write_analog(speed)
            pin8.write_digital(0)
            pin14.write_analog(speed)
            pin12.write_digital(0)

    def backward(self, speed):
        if (speed > 1023) or (speed < 1):
            print("Error, speed must be a number 1-1023")
            display.scroll("Speed must be a number 1-1023")
        else:
            pin16.write_digital(0)
            pin8.write_analog(speed)
            pin14.write_digital(0)
            pin12.write_analog(speed)

    def left(self, speed):
        if (speed > 1023) or (speed < 1):
            print("Error, speed must be a number 1-1023")
            display.scroll("Speed must be a number 1-1023")
        else:
            pin14.write_analog(0)
            pin12.write_analog(0)
            pin16.write_analog(speed)
            pin8.write_digital(0)

    def right(self, speed):
        if (speed > 1023) or (speed < 1):
            print("Error, speed must be a number 1-1023")
            display.scroll("Speed must be a number 1-1023")
        else:
            pin16.write_analog(0)
            pin8.write_analog(0)
            pin14.write_analog(speed)
            pin12.write_digital(0)

    def stop(self, brake=True):
        if brake==True:
            pin16.write_analog(1023)
            pin8.write_analog(1023)
            pin14.write_analog(1023)
            pin12.write_analog(1023)
        else:
            pin16.write_analog(0)
            pin8.write_analog(0)
            pin14.write_analog(0)
            pin12.write_analog(0)


class BitBotXLDistanceSensor():

    def distance(self):
        DISTANCE_SENSOR_PIN.write_digital(1)
        utime.sleep_us(10)
        DISTANCE_SENSOR_PIN.write_digital(0)

        while DISTANCE_SENSOR_PIN.read_digital() == 0:
            pulse_start = utime.ticks_us()
        while DISTANCE_SENSOR_PIN.read_digital() == 1:
            pulse_end = utime.ticks_us()

        pulse_duration = pulse_end - pulse_start
        distance = int(0.01715 * pulse_duration)
        return distance


