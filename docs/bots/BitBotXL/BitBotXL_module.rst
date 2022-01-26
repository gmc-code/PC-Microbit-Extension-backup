====================================================
BitBotXL module
====================================================

This is a tutorial in which a module for the BitBotXL will be written.

| The module will broken into sections based on functionality. 
| Each section of code in the module will be in a class code block with all the relevant functions and methods for that functionality within that class:

* a class for **motors** using pin16, pin8, pin14, pin12
* a class for **ultrasonic sensor** using pin15
* a class for **line sensors** using I2C
* a class for the **LEDS** using pin13
* a class for the **buzzer** using pin0
* a class for **light sensors** using pin1 and pin2

=======  ===========================
 Pin     Purpose
=======  ===========================
 pin0    Buzzer
 pin1    Right Light Sensor
 pin2    Left Light Sensor
 pin8    Left Motor Backward
 pin12   Right Motor Backward
 pin13   12x LEDs
 pin14   Right Motor
 pin15   Ultrasonic
 pin16   Left Motor
=======  ===========================

| I2C address 0x1c  (28)
| Left Line Sensor bit 0
| Right Line Sensor bit 1


