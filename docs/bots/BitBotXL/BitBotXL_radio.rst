====================================================
BitBotXL radio
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
| The code displays the message on the microbit for testing purposes.


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
                display.show("B")
            elif y_reading < -200:
                radio.send("F")
                display.show("F")
            else:
                radio.send("X")
                display.show("X")
        elif button_b.was_pressed():
            x_reading = accelerometer.get_x()
            if x_reading > 200:
                radio.send("R")
                display.show("R")
            elif x_reading < -200:
                radio.send("L")
                display.show("L")
            else:
                radio.send("-")
                display.show("-")

----

Radio for microbit on bot
----------------------------

| The code below gives one possible way the bot may respond to radio messages from the code above.


.. code-block:: python


    from microbit import *
    import radio
    import BitBotXL
    import neopixel


    radio.config(group=8)  # 0-255
    radio.on()
    
    buggy = BitBotXL.BitBotXLMotors()
    
    buggyLights = neopixel.NeoPixel(pin13, 12)
    dull_blue = [20, 20, 25]
    dull_red = [25, 0, 0]

    def light_display():
        #even lights 0 to 10
        for i in range(0, 12, 2):
            buggyLights[i] = dull_blue
        # odd lights 1 to 11
        for i in range(1, 13, 2):
            buggyLights[i] = dull_red
        buggyLights.show()
        sleep(2000)
        buggyLights.clear()


    while True:
        incoming_message = radio.receive()
        if incoming_message is not None:
            display.show(incoming_message)
            if incoming_message == "B":
                buggy.backward(5, duration=1000)
                display.show("B")
            elif incoming_message == "F":
                buggy.forward(5, duration=1000)
                display.show("F")
            elif incoming_message == "X":
                buggy.stop()
                display.show("X")
            elif incoming_message == "R":
                buggy.right(speed=3, tightness=2, duration=1000)
                display.show("R")
            elif incoming_message == "L":
                buggy.left(speed=3, tightness=2, duration=1000)
                display.show("L")
            elif incoming_message == "-":
                light_display()
                display.show("-")

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
                # display.show("B")
            elif y_reading < -200:
                radio.send("F")
                # display.show("F")
            else:
                radio.send("X")
                # display.show("X")
        elif button_b.was_pressed():
            x_reading = accelerometer.get_x()
            if x_reading > 200:
                radio.send("R")
                # display.show("R")
            elif x_reading < -200:
                radio.send("L")
                # display.show("L")
            else:
                radio.send("-")
                # display.show("-")


----

Radio for microbit on bot
----------------------------

| Increase the speed to maximum.

.. code-block:: python

    from microbit import *
    import radio
    import BitBotXL
    import neopixel

    radio.config(group=8)  # 0-255
    radio.on()

    buggy = BitBotXL.BitBotXLMotors()
    buggyLights = neopixel.NeoPixel(pin13, 12)
    dull_blue = [20, 20, 25]
    dull_red = [25, 0, 0]

    def light_display():
        #even lights 0 to 10
        for i in range(0, 12, 2):
            buggyLights[i] = dull_blue
        # odd lights 1 to 11
        for i in range(1, 13, 2):
            buggyLights[i] = dull_red
        buggyLights.show()
        sleep(2000)
        buggyLights.clear()
            

    while True:
        incoming_message = radio.receive()
        if incoming_message is not None:
            # display.show(incoming_message)
            if incoming_message == "B":
                buggy.backward(10, duration=1000)
                # display.show("B")
            elif incoming_message == "F":
                buggy.forward(10, duration=1000)
                # display.show("F")
            elif incoming_message == "X":
                buggy.stop()
                # display.show("X")
            elif incoming_message == "R":
                buggy.right(speed=10, tightness=2, duration=1000)
                # display.show("R")
            elif incoming_message == "L":
                buggy.left(speed= 10, tightness=2, duration=1000)
                # display.show("L")
            elif incoming_message == "-":
                light_display()
                # display.show("-")

----

Radio Racing
----------------------------

.. admonition:: Tasks

    #. Create an obstacle course and race another bot using radio controls
    #. Add a distance sensor with automatic reversal from objects within a small distance.


