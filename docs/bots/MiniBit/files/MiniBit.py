# MiniBit module for motors, and distance sensing
# requires microbit v2
# GMC-code; 2022
# The MIT License (MIT)

# A microbit v2 micropython module
# speed from -10 to 10


from microbit import *
import utime

# constants

DISTANCE_SENSOR_PIN = pin15
LEFT_FWD_PIN = pin12
LEFT_BWD_PIN = pin8
RIGHT_FWD_PIN = pin14
RIGHT_BWD_PIN = pin16

 
class MiniBitMotors:

    def __init__(self):
        # left and right motor adjustments
        self.dec_left = 1
        self.dec_right = 1

    def stop_left(self):
        LEFT_FWD_PIN.write_digital(0)
        LEFT_BWD_PIN.write_digital(0)

    def stop_right(self):
        RIGHT_FWD_PIN.write_digital(0)
        RIGHT_BWD_PIN.write_digital(0)

    def stop(self):
        self.stop_left()
        self.stop_right()

    def set_bias_correction(self, direction='left', percent=0):
        """Set left/right bias to match motors."""
        factor = (percent + 100) / 100
        if direction == 'left':
            self.dec_left = factor
        elif direction == 'right':
            self.dec_right = factor

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

    def left_motor(self, speed=2, duration=None):
        an_speed = self._analog_speed(speed / self.dec_left)
        # an_speed = self._analog_speed(speed)
        # display.scroll(an_speed, delay=60)
        if (speed > 0):
            LEFT_FWD_PIN.write_analog(an_speed)
            LEFT_BWD_PIN.write_digital(0)
        else:
            LEFT_FWD_PIN.write_digital(0)
            LEFT_BWD_PIN.write_analog(an_speed)
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop_left()

    def right_motor(self, speed=2, duration=None):
        an_speed = self._analog_speed(speed / self.dec_right)
        # an_speed = self._analog_speed(speed)
        # display.scroll(an_speed, delay=60)
        if (speed > 0):
            RIGHT_FWD_PIN.write_analog(an_speed)
            RIGHT_BWD_PIN.write_digital(0)
        else:
            RIGHT_FWD_PIN.write_digital(0)
            RIGHT_BWD_PIN.write_analog(an_speed)
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop_right()

    def forward(self, speed=2, duration=None):
        self.right_motor(speed)
        self.left_motor(speed)
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop()

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
        DISTANCE_SENSOR_PIN.write_digital(1)
        utime.sleep_us(10)
        DISTANCE_SENSOR_PIN.write_digital(0)

        while DISTANCE_SENSOR_PIN.read_digital() == 0:
            pulse_start = utime.ticks_us()
        while DISTANCE_SENSOR_PIN.read_digital() == 1:
            pulse_end = utime.ticks_us()

        try:
            pulse_duration = pulse_end - pulse_start
        except ValueError:
            pulse_duration = 0
        else:
            pulse_duration = 0
            
        distance = int(0.01715 * pulse_duration)
        return distance

