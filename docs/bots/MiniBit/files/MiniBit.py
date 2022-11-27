# MiniBit module for motors, and distance sensing
# requires microbit v2
# GMC-code; 2022
# The MIT License (MIT)

# A microbit v2 micropython module
# speed from -10 to 10


from microbit import *
import utime

# constants
LMF = pin12
LMB = pin8
RMF = pin16
RMB = pin14
DSP = pin15
                   
class MiniBitMotors:

    def __init__(self):
        # no need to do anything
        pass

    def stop(self):
        LMF.write_digital(0)
        LMB.write_digital(0)
        RMF.write_digital(0)
        RMB.write_digital(0)

    @staticmethod
    def _analog_speed(speed):
        # input speed = -10 to 0 to 10
        # output = 0 to 1023
        if speed < 0 and speed >= -10:
            return - int((speed * 100) - 23)
        elif speed > 0 and speed <= 10:
            return int((speed * 100) + 23)
        else:
            return 0

    def scale(from_value, from_min, from_max, to_min, to_max):
        return int(((from_value - from_min) / (from_max - from_min)) * (to_max - to_min) + to_min)

    def speed_scaled(speed):
        return scale(speed, 0, 10, 0, 1023)
        
    def forwards(speed=2, duration=None):
        analog_speed = speed_scaled(speed)
        LMF.write_analog(analog_speed)
        LMB.write_digital(0)
        RMF.write_analog(analog_speed)
        RMB.write_digital(0)
        if duration is not None:
            utime.sleep_ms(duration)
            stop()

    def backward(self, speed=2, duration=None):
        self.right_motor(-speed)
        self.left_motor(-speed)
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop()

    @staticmethod
    def _inner_turn_speed(speed, tightness=2):
        return speed / tightness

    def left(self, speed=2, tightness=2, duration=None):
        # right motor faster than left
        # display.scroll(outer_speed)
        # display.scroll(tightness)
        inner_speed = self._inner_turn_speed(speed, tightness)
        # display.scroll(inner_speed)
        self.left_motor(inner_speed)
        self.right_motor(speed)
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop()

    def right(self, speed=2, tightness=2, duration=None):
        # left motor faster than right
        inner_speed = self._inner_turn_speed(speed, tightness)
        self.left_motor(speed)
        self.right_motor(inner_speed)
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop()

    def spin_left(self, speed=2, duration=None):
        self.left_motor(-speed)
        self.right_motor(speed)
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop()

    def spin_right(self, speed=2, duration=None):
        self.left_motor(speed)
        self.right_motor(-speed)
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop()


class MiniBitDistanceSensor():

    def distance(self):
        DSP.write_digital(1)
        utime.sleep_us(10)
        DSP.write_digital(0)

        while DSP.read_digital() == 0:
            pulse_start = utime.ticks_us()
        while DSP.read_digital() == 1:
            pulse_end = utime.ticks_us()

        try:
            pulse_duration = pulse_end - pulse_start
        except ValueError:
            pulse_duration = 0
        else:
            pulse_duration = 0

        distance = int(0.01715 * pulse_duration)
        return distance

