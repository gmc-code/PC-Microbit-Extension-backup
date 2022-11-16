====================================================
MoveMotor radio
====================================================


Unique groups
----------------------

| Use ``radio.config(group=8)`` to set unique groups in the room.
| Make sure all microbits using a bot have the same group number (0-255).
| Edit the code below to set the group.
| The buggy **speeds** and **durations** can also be edited for different responses.

----

Radio for controller
----------------------

| The code below gives 3 messages for the A button based on forward and back tilting.
| The code below gives 3 messages for the B button based on sideways tilting.
| The code dispalys the message on the microbit for testing purposes.


.. code-block:: python

    from microbit import *
    import radio


    radio.config(group=8)  # 0-255
    radio.on()

    while True:
        if button_a.was_pressed():
            y_reading = accelerometer.get_y()
            if y_reading > 200:
                radio.send("B")
                display.scroll("B")
            elif y_reading < -200:
                radio.send("F")
                display.scroll("F")
            else:
                radio.send("X")
                display.scroll("X")
        elif button_b.was_pressed():
            x_reading = accelerometer.get_x()
            if x_reading > 200:
                radio.send("R")
                display.scroll("R")
            elif x_reading < -200:
                radio.send("L")
                display.scroll("L")
            else:
                radio.send("-")
                display.scroll("-")

----

Radio for microbit on bot
----------------------------

| The code below gives one possible way the bot may respond to radio messages from the code above.


.. code-block:: python


    from microbit import *
    import radio
    import MOVEMotor
    import neopixel


    np = neopixel.NeoPixel(pin8, 4)
    buggy = MOVEMotor.MOVEMotorMotors()
    

    radio.config(group=8)  # 0-255
    radio.on()

    while True:
        incoming_message = radio.receive()
        if incoming_message is not None:
            display.scroll(incoming_message)
            if incoming_message == "B":
                buggy.backward(5, duration=1000)
                display.scroll("B")
            elif incoming_message == "F":
                buggy.forward(5, duration=1000)
                display.scroll("F")
            elif incoming_message == "X":
                buggy.stop()
                display.scroll("X")
            elif incoming_message == "R":
                buggy.right(speed=3, tightness=2, duration=1000)
                display.scroll("R")
            elif incoming_message == "L":
                buggy.left(speed=3, tightness=2, duration=1000)
                display.scroll("L")
            elif incoming_message == "-":
                display.scroll("-")

----

Reducing delays by commenting out displays
--------------------------------------------

| Comment out the display calls so reduce delays in response.

----

Radio for controller
----------------------

.. code-block:: python

    from microbit import *
    import radio

    radio.config(group=8)  # 0-255
    radio.on()

    while True:
        if button_a.was_pressed():
            y_reading = accelerometer.get_y()
            if y_reading > 200:
                radio.send("B")
                # display.scroll("B")
            elif y_reading < -200:
                radio.send("F")
                # display.scroll("F")
            else:
                radio.send("X")
                # display.scroll("X")
        elif button_b.was_pressed():
            x_reading = accelerometer.get_x()
            if x_reading > 200:
                radio.send("R")
                # display.scroll("R")
            elif x_reading < -200:
                radio.send("L")
                # display.scroll("L")
            else:
                radio.send("-")
                # display.scroll("-")


----

Radio for microbit on bot
----------------------------

| Increase the speed to maximum.

.. code-block:: python

    from microbit import *
    import radio
    import MOVEMotor


    # setup buggy
    buggy = MOVEMotor.MOVEMotorMotors()
    

            
    radio.config(group=10)  # 0-255
    radio.on()

    while True:
        incoming_message = radio.receive()
        if incoming_message is not None:
            # display.scroll(incoming_message)
            if incoming_message == "B":
                buggy.backward(10, duration=1000)
                # display.scroll("B")
            elif incoming_message == "F":
                buggy.forward(10, duration=1000)
                # display.scroll("F")
            elif incoming_message == "X":
                buggy.stop()
                # display.scroll("X")
            elif incoming_message == "R":
                buggy.right(speed=10, tightness=2, duration=1000)
                # display.scroll("R")
            elif incoming_message == "L":
                buggy.left(speed= 10, tightness=2, duration=1000)
                # display.scroll("L")
            elif incoming_message == "-":

                # display.scroll("-")

----

Radio Racing
----------------------------

.. admonition:: Tasks

    #. Create an obstacle course and race another bot using radio controls
    #. Add a distance sensor with automatic reversal from objects within a small distance.


