====================================================
BitBotXL radio
====================================================


Unique groups
----------------------

| Use ``radio.config(group=8)`` to set unique groups in the room.
| Make sure all microbits using a bot have the same group number (0-255).
| Edit the code below to set the group.
| The buggy speeds can also be edited for different responses.

----

Radio for controller
----------------------

| The code below gives 3 messages for the A button based on forward and back tilting.
| The code below gives 3 messages for the B button based on sideways tilting.


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

| The code below gives one possible the bot may respond to radio messages from the code above.


.. code-block:: python

    from microbit import *
    import radio
    import BitBotXL
    import neopixel

    buggy = BitBotXL.BitBotXLMotors()
    buggyLights = neopixel.NeoPixel(pin13, 12)
    dull_blue = [20, 20, 25]
    dull_red = [25, 0, 0]


    radio.config(group=8)  # 0-255
    radio.on()

    while True:
        incoming_message = radio.receive()
        if incoming_message is not None:
            display.scroll(incoming_message)
            if incoming_message == "B":
                buggy.backward(5)
                display.scroll("B")
            elif incoming_message == "F":
                buggy.forward(5)
                display.scroll("F")
            elif incoming_message == "X":
                buggy.stop()
                display.scroll("X")
            elif incoming_message == "R":
                buggy.stop_left()
                buggy.right_motor(5)
                display.scroll("R")
            elif incoming_message == "L":
                buggy.stop_right()
                buggy.left_motor(5)
                display.scroll("L")
            elif incoming_message == "-":
                for i in range(6):
                    buggyLights[i] = dull_blue
                for i in range(6, 12):
                    buggyLights[i] = dull_red
                buggyLights.show()
                sleep(2000)
                buggyLights.clear()
                display.scroll("-")
