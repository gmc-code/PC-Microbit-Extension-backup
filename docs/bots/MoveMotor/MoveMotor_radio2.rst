====================================================
MoveMotor radio 2
====================================================

Unique groups
----------------------

| Use ``radio.config(group=8)`` to set unique groups in the room.
| Make sure all microbits using a bot have the same group number (0-255).
| Edit the code below to set the group.

----

Using tilting for variable speeds
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Radio for controller
----------------------


| The code below requires A button pressing for motor control.
| No durations are set, so the motors will continue running with the last instruction they receive.

| To stop, send X.

| For increasing speed forward, send: F, G, H. 
| Tilt forward a bit, F is sent, and a slow speed results.
| Tilt forward a bit more, G is sent, and a medium speed results.
| Tilt forward a lot, H is sent, and a fast speed results.

| For increasing speed backward, send: B, C, D
| Tilt backward.

| For increasing speed left, send: L, M, N
| Tilt left.

| For increasing speed right, send: R, S, T
| Tilt right.


.. code-block:: python

    from microbit import *
    import radio

    radio.config(group=8)  # 0-255
    radio.on()


    while True:
        sleep(100)
        if button_a.is_pressed():
            y_reading = accelerometer.get_y()
            x_reading = accelerometer.get_x()
            if -300 < y_reading < 300 and -300 < x_reading < 300:
                msg = "X"
            elif -200 < x_reading < 200:
                if y_reading > 700:
                    msg = "D"
                elif y_reading > 500:
                    msg = "C"
                elif y_reading > 300:
                    msg = "B"
                elif y_reading < -700:
                    msg = "H"
                elif y_reading < -500:
                    msg = "G"
                elif y_reading < -300:
                    msg = "F"
            else:
                if x_reading > 700:
                    msg = "T"
                elif x_reading > 500:
                    msg = "S"
                elif x_reading > 300:
                    msg = "R"
                elif x_reading < -700:
                    msg = "N"
                elif x_reading < -500:
                    msg = "M"
                elif x_reading < -300:
                    msg = "L"
            radio.send(msg)
            display.show(msg)


----

Radio for microbit on bot
----------------------------

| There are 3 speed settings, 2, 5, and 10.
| When turning, the slowest speed has a tighter turn; the fastest speed has a less tight turnning circle.


.. code-block:: python

    from microbit import *
    import radio
    import MOVEMotor


    
    radio.config(group=8)  # 0-255
    radio.on()

    # setup buggy
    buggy = MOVEMotor.MOVEMotorMotors()

            
    while True:
        incoming_message = radio.receive()
        if incoming_message is not None:
            if incoming_message == "B":
                buggy.backward(speed=2)
            elif incoming_message == "C":
                buggy.forward(speed=5)
            elif incoming_message == "D":
                buggy.forward(speed=10)
            elif incoming_message == "F":
                buggy.forward(speed=2)
            elif incoming_message == "G":
                buggy.forward(speed=5)
            elif incoming_message == "H":
                buggy.forward(speed=10)
            elif incoming_message == "X":
                buggy.stop()
            elif incoming_message == "L":
                buggy.left(speed=2, radius=5)
            elif incoming_message == "M":
                buggy.left(speed=5, radius=10)
            elif incoming_message == "N":
                buggy.left(speed=10, radius=25)
            elif incoming_message == "R":
                buggy.right(speed=2, radius=5)
            elif incoming_message == "S":
                buggy.right(speed=5, radius=10)
            elif incoming_message == "T":
                buggy.right(speed=10, radius=25)


----

Turning backwards
----------------------------

.. admonition:: Tasks

    #. Add B button pressing to allow backward movement while turning.

