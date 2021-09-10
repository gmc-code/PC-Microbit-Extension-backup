====================================================
TiltPixels
====================================================

Game design
--------------------

| Code a game to find hidden pixels on the display by titling the microbit.
| Use a class object for the game's pixels.
| The (x,y) coordinates of each pixel are in the diagram below.

.. image:: images/microbit_coords.png
    :scale: 100 %
    :align: center
    :alt: coordinates


#. Set up the game object (initialize an instance of the class)
    #. Set between 2 and 10 random pixels to be found.
    #. Start from a random pixel and display it brightly then faintly.
#. Repeat the following steps:
    #. Use the accelerometer to detect a tilt and move the pixel.
    #. If all the pixels have been found then:
        a. Scroll the score.
        b. Set up the game object again and play again.


| The outline for the code uses the class, ``TiltPixels()``, for the game object.
| 4 methods will be used below in the running of the code.

#. ``.tilt()`` will move a bright pixel in the direction of tilt
#. ``.filled()`` will compare the hidden pixels with those arrived at by tilting
#. ``.answer()`` will display the originally hidden pixels brightly and the other chosen pixels dimly.
#. ``.score()`` will calculate the score


.. code-block:: python

    from microbit import *


    mypix = TiltPixels()
    while True:
        mypix.tilt()
        sleep(200)
        if mypix.filled():
            mypix.answer()
            display.scroll(mypix.score())
            mypix = TiltPixels()

----

The TiltPixels class
------------------------

.. py:class:: TiltPixels(x_position=random.randint(0, 4), y_position=random.randint(0, 4))

    | Set up the game object to control the pixels displayed and keep track of them.
    | The starting pixel is (x_position, y_position).
    | ``x_position`` and  ``y_position`` are optional. They are both integers from 0 to 4.
    | ``x_position`` by default will be a random integer from 0 to 4.
    | ``y_position`` by default will be a random integer from 0 to 4.

| The code below imports the random module and sets up the game object.

.. code-block:: python

    from microbit import *
    import random


    mypix = TiltPixels()

----

