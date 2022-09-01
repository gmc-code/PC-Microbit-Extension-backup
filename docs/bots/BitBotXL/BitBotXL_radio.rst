====================================================
BitBotXL radio
====================================================


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
                display.scroll("B")
                radio.send("B")
            elif y_reading < -200:
                display.scroll("F")
                radio.send("F")
            else:
                display.scroll("X")
                radio.send("X")
        elif button_b.was_pressed():
            x_reading = accelerometer.get_x()
            if x_reading > 200:
                display.scroll("R")
                radio.send("R")
            elif x_reading < -200:
                display.scroll("L")
                radio.send("L")
            else:
                display.scroll("-")
                radio.send("-")


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
                display.scroll("B")
                buggy.backward(5)
            elif incoming_message == "F":
                display.scroll("F")
                buggy.forward(5)
            elif incoming_message == "X":
                display.scroll("X")
                buggy.stop()
            elif incoming_message == "R":
                display.scroll("R")
                buggy.stop_left()
                buggy.right_motor(5)
            elif incoming_message == "L":
                display.scroll("L")
                buggy.stop_right()
                buggy.left_motor(5)
            elif incoming_message == "-":
                display.scroll("-")
                for i in range(6):
                    buggyLights[i] = dull_blue
                for i in range(6, 12):
                    buggyLights[i] = dull_red
                buggyLights.show()
                sleep(2000)
                buggyLights.clear()
