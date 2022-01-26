====================================================
BitBotXL buzzer
====================================================

Using the buzzer
------------------------------

| The buzzer is on pin0.
| It can be turned on using: ``pin0.write_digital(1)``.
| It can be turned off using: ``pin0.write_digital(0)``.

To turn on the buzzer for a specific time, put in a sleep between turning it on and turning it off. The code below has a sleep for 1000ms, so that the buzzer is on for 1 sec.

.. code-block:: python

    from microbit import *

    pin0.write_digital(1)
    sleep(1000)
    pin0.write_digital(0)

----

.. admonition:: Tasks

    #. Write code to turn on the buzzer for half a second.
    #. Write code, using a for loop, to make 3 half second buzzer sounds with 1 second between each of them.

----   

Packaging into a class
------------------------------

| The class, ``class BitBotXLBuzzer()``, is used for the code related to the buzzer.
| The code to drive the buzzer is placed in a function, ``buzz``.
| The function will have a parameter, ``duration``,  which sets the duration of the buzzer.

| Firstly, the code above is placed inside a function.
| The sleep value is replaced with the ``duration`` parameter.
| The ``self`` parameter must be included for a regular method in the class.
| Instead of ``def buzz(duration):``, ``def buzz(self, duration):`` is required.

.. code-block:: python

    class BitBotXLBuzzer():

        def buzz(self, duration):
            """Sound a buzz for duration milliseconds."""
            pin0.write_digital(1)
            sleep(duration)
            pin0.write_digital(0)


----

Using the class
----------------------------------------

.. py:class:: BitBotXLBuzzer() 

    | Set up the buggy's buzzer for use.
    | Use ``buzzer = BitBotXL.BitBotXLBuzzer()`` to use the buggy's buzzer.

| The code below imports the BitBotXL module and sets up the buzzer.

.. code-block:: python

    from microbit import *
    import BitBotXL


    # setup the buzzer
    buzzer = BitBotXL.BitBotXLBuzzer()


----

Using the buzzer method
----------------------------------------

.. py:method:: buzz(duration)

    Activates teh buzzer for teh specified duration in milliseconds.


| The code below, uses ``buzzer.buzz(duration)`` to make a buzz.

.. code-block:: python

    from microbit import *
    import BitBotXL


    # setup the buzzer
    buzzer = BitBotXL.BitBotXLBuzzer()

    buzzer.buzz(1000)


----

.. admonition:: Tasks

    #. Write code using a while True loop to make a 500ms buzz every 2 seconds.
    #. Write code using a for loop to make buzz sounds of 100, 200, 300 and 400ms separated by a 500ms sleep.
