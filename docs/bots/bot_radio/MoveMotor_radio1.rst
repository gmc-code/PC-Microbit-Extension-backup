====================================================
MoveMotor radio 1
====================================================

Redesign to use tilting for speeds
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Radio for controller
----------------------

| For increasing speed forward send: F, G, H
| For increasing speed backward send: B, C, D
| For increasing speed left send: F, G, H
| For increasing speed forward send: F, G, H

.. code-block:: python

    from microbit import *
    import radio

    radio.config(group=8)  # 0-255
    radio.on()


    while True:
        # if button_a.was_pressed():
        sleep(100)
        y_reading = accelerometer.get_y()
        x_reading = accelerometer.get_x()
        if -300 < y_reading < 300 and -300 < x_reading < 300:
            display.show("X")
        elif -200 < x_reading < 200:
            if y_reading > 700:
                display.show("D")
            elif y_reading > 500:
                display.show("C")
            elif y_reading > 300:
                display.show("B")
            elif y_reading < -700:
                display.show("H")
            elif y_reading < -500:
                display.show("G")
            elif y_reading < -300:
                display.show("F")
        else:     
            if x_reading > 700:
                display.show("T")
            elif x_reading > 500:
                display.show("S")
            elif x_reading > 300:
                display.show("R")
            elif x_reading < -700:
                display.show("N")
            elif x_reading < -500:
                display.show("M")
            elif x_reading < -300:
                display.show("L")


----

Radio for microbit on bot
----------------------------

| Increase the speed to maximum.

.. code-block:: python

    from microbit import *
    import radio
    import MOVEMotor


    
    radio.config(group=8)  # 0-255
    radio.on()

    # setup buggy
    buggy = MOVEMotor.MOVEMotorMotors()

            
    while True:
        msg = radio.receive()
        if msg is not None:
            if msg == "B":
                buggy.backward(2, duration=1000)
            elif msg == "C":
                buggy.forward(5, duration=1000)
            elif msg == "D":
                buggy.forward(10, duration=1000)
            elif msg == "F":
                buggy.forward(2, duration=1000)
            elif msg == "G":
                buggy.forward(5, duration=1000)
            elif msg == "H":
                buggy.forward(10, duration=1000)
            elif msg == "X":
                buggy.stop()
            elif msg == "L":
                buggy.left(speed=2, radius=5, duration=1000)
            elif msg == "M":
                buggy.left(speed=5, radius=10, duration=1000)
            elif msg == "N":
                buggy.left(speed=10, radius=25, duration=1000)
            elif msg == "R":
                buggy.right(speed=2, radius=5, duration=1000)
            elif msg == "S":
                buggy.right(speed=5, radius=10, duration=1000)
            elif msg == "T":
                buggy.right(speed=10, radius=25, duration=1000)


