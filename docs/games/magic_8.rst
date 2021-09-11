====================================================
Magic 8-ball simulation
====================================================

Game design
--------------------

| The user asks a yes–no question then shakes the microbit to receive an answer.
| The standard responses are in a list, RESPONSES. (The convention is to use capitals for a constant.)
| A random choice from the list is obtained using the ``random.choice(RESPONSES)``

Specific Syntax
--------------------

.. py:function::  random.choice(sequence)

    Return a random element from a sequence such as a list.

.. py:function::  microbit.accelerometer.was_gesture(gesture)

    Return True or False to indicate if the named gesture was active since the last call.

----

Game code
---------------------------------

| The game code is below.

.. code-block:: python


    """Magic_8 simulation see responses at https://en.wikipedia.org/wiki/Magic_8-Ball"""

    from microbit import *
    import random


    RESPONSES = [
        "It is certain",
        "It is decidedly so",
        "Without a doubt",
        "Yes, definitely",
        "You may rely on it",
        "As I see it, yes",
        "Most likely",
        "Outlook good",
        "Yes",
        "Signs point to yes",
        "Reply hazy try again",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful",
    ]

    while True:
        display.show("8")
        if accelerometer.was_gesture("shake"):
            display.clear()
            sleep(500)
            display.scroll(random.choice(RESPONSES), delay=100)





----

.. admonition:: Tasks

    #. Modify the code to require a button press instead of a shake.
    #. Divide up the responses into positive responses and negative responses. Display a positive response when the A button is pressed and a negative response when the B button is pressed.


