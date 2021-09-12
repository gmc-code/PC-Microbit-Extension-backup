====================================================
Magic 8-ball simulation
====================================================

Game design
--------------------

| The user asks a yes–no question then shakes the microbit to receive an answer.
| The standard responses are in a list, RESPONSES. (The convention is to use capitals for a constant.)
| A random choice from the list is obtained using ``random.choice(RESPONSES)``.

Specific Syntax
--------------------

.. py:function::  random.choice(sequence)

    Return a random element from a sequence such as a list.

.. py:function::  microbit.accelerometer.was_gesture(gesture)

    Return True or False to indicate if the named gesture was active since the last call.

----

Simple Game code
---------------------------------

| The first version of the game code is below.

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
            sleep(1000)
            display.scroll(random.choice(RESPONSES), delay=120)

----

.. admonition:: Tasks

    #. Modify the code to require a button press instead of a shake.
    #. Divide up the responses into positive responses and negative responses. Display a positive response when the A button is pressed and a negative response when the B button is pressed.

----

Converting to using a class
---------------------------------

| The class version of the game code is below.
| The ``__init__`` method has the responses list.
| The ``run_game`` method has the game code that was previously within the body of the while loop.
| ``m8 = Magic8()`` instantiates the class by creating a copy of the class which inherits all the class attributes and methods.
| ``m8.run_game()`` calls the ``run_game`` method on the game object to run the game.

.. code-block:: python

    """Magic_8 see standard responses at https://en.wikipedia.org/wiki/Magic_8-Ball"""

    from microbit import *
    import random


    class Magic8:
        def __init__(self):
            self.RESPONSES = [
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
                "Outlook not so good",0
                "Very doubtful",
            ]
            
        def run_game(self):
            display.show("8")
            if accelerometer.was_gesture("shake"):
                display.clear()
                sleep(1000)
                display.scroll(random.choice(self.RESPONSES), delay=120)

    while True:
        m8 = Magic8()
        m8.run_game()


----

.. admonition:: Tasks

    #. Modify the code to require a button press instead of a shake.
    #. Divide up the responses into positive responses and negative responses. Display a positive response when the A button is pressed and a negative response when the B button is pressed.

