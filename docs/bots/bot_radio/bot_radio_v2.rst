====================================================
Bot radio v2
====================================================

| This uses more settings for the motor control by titlting to different degrees.
| Three speed settings are used below.

----

Unique groups
----------------------

| Use ``radio.config(group=8)`` to set unique groups in the room.
| Make sure all microbits using a bot have the same group number (0-255).
| Edit the code below to set the group.
| The buggy **speeds** and **durations** can also be edited for different responses.

----

Radio for controller
----------------------

| The code below gives messages based on forward - backward tilting and sideways tilting.
| The code displays the message on the microbit for testing purposes.
| For the forward and backward tilting, make sure not to tilt the microbit sideways.

| If the microbit is level, ``-200 <= y_reading <= 200 and -200 <= x_reading <= 200``, send an "X", to stop.

| For increasing speed forward, send: F, G, H. 
| Tilt forward a bit, F is sent, and a slow speed results.
| Tilt forward a bit more, G is sent, and a medium speed results.
| Tilt forward a lot, H is sent, and a fast speed results.

| For increasing speed backward, send: B, C, D
| Tilt backward more and more.

| For increasing speed left, send: L, M, N
| Tilt left more and more.

| For increasing speed right, send: R, S, T
| Tilt right more and more.


.. code-block:: python

    from microbit import *
    import radio

    radio.config(group=8)  # 0-255
    radio.on()


    while True:
        sleep(50)
        y_reading = accelerometer.get_y()
        x_reading = accelerometer.get_x()
        # level sideways only
        if -200 <= y_reading <= 200 and -200 <= x_reading <= 200:
            msg = "X"
        # level sideways only
        elif -200 <= x_reading <= 200:
            if y_reading > 700:
                msg = "D"
            elif y_reading > 500:
                msg = "C"
            elif y_reading > 200:
                msg = "B"
            elif y_reading < -700:
                msg = "H"
            elif y_reading < -500:
                msg = "G"
            elif y_reading < -200:
                msg = "F"
        else:
            if x_reading > 700:
                msg = "T"
            elif x_reading > 500:
                msg = "S"
            elif x_reading > 200:
                msg = "R"
            elif x_reading < -700:
                msg = "N"
            elif x_reading < -500:
                msg = "M"
            elif x_reading < -200:
                msg = "L"
        radio.send(msg)
        display.show(msg)

----

Radio for microbit on BitBotXL
--------------------------------------

| The code below moves the BitBotXL at maximum speed, since its top speed is relatively slow.
| The tightness of 5 gives a tight turn.
| High turning speed settings are used belwo for bset contorl based on testing.

.. code-block:: python


    from microbit import *
    import radio
    import BitBotXL


    radio.config(group=8)  # 0-255
    radio.on()

    buggy = BitBotXL.BitBotXLMotors()


    while True:
        sleep(50)
        msg = radio.receive()
        if msg is not None:
            display.show(msg)
            if msg == "B":
                buggy.backward(speed=5)
            elif msg == "C":
                buggy.backward(speed=8)
            elif msg == "D":
                buggy.backward(speed=10)
            elif msg == "F":
                buggy.forward(speed=5)
            elif msg == "G":
                buggy.forward(speed=8)
            elif msg == "H":
                buggy.forward(speed=10)
            elif msg == "X":
                buggy.stop()
            elif msg == "L":
                buggy.left(speed=10, tightness=5)
            elif msg == "M":
                buggy.left(speed=10, tightness=3)
            elif msg == "N":
                buggy.left(speed=10, tightness=2)
            elif msg == "R":
                buggy.right(speed=10, tightness=5)
            elif msg == "S":
                buggy.right(speed=10, tightness=3)
            elif msg == "T":
                buggy.right(speed=10, tightness=2)

----

Radio for microbit on MOVEMotor
--------------------------------

| The code below moves the MOVEMotor at medium speed, since its top speed is relatively fast.
| The radius of 5 gives a tight turn.
| Low urning speed settings are used below for best control based on testing.


.. code-block:: python

    from microbit import *
    import radio
    import MOVEMotor


    radio.config(group=8)  # 0-255
    radio.on()

    buggy = MOVEMotor.MOVEMotorMotors()

    while True:
        sleep(50)
        msg = radio.receive()
        if msg is not None:
            display.show(msg)
            if msg == "B":
                buggy.backward(speed=5)
            elif msg == "C":
                buggy.backward(speed=8)
            elif msg == "D":
                buggy.backward(speed=10)
            elif msg == "F":
                buggy.forward(speed=5)
            elif msg == "G":
                buggy.forward(speed=8)
            elif msg == "H":
                buggy.forward(speed=10)
            elif msg == "X":
                buggy.stop()
            elif msg == "L":
                buggy.left(speed=2, radius=5)
            elif msg == "M":
                buggy.left(speed=3, radius=15)
            elif msg == "N":
                buggy.left(speed=4, radius=25)
            elif msg == "R":
                buggy.right(speed=2, radius=5)
            elif msg == "S":
                buggy.right(speed=3, radius=15)
            elif msg == "T":
                buggy.right(speed=4, radius=25)
            


----

Radio Racing
----------------------------

.. admonition:: Tasks

    #. Create an obstacle course and race another bot using radio controls.
    #. Modify the speed settings to suit the obstacle course.
    #. Add a variable to keep track of the last msg sent and only send a new msg if it is different to the last msg.



