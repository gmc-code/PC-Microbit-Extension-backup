====================================================
TiltPixels
====================================================

Game design
--------------------

| TiltPixels is a game to find hidden pixels on the display by titling the microbit.
| A class is used to run the game.
| A set will be used to keep track of the pixels visited by tilting.
| The (x,y) coordinates of each pixel are in the diagram below.

.. image:: images/microbit_coords.png
    :scale: 100 %
    :align: center
    :alt: coordinates


#. Set up the game object (initialize an instance of the class)
    a. Set between 2 and 10 random pixels to be found.
    b. Start from a random pixel and display it brightly then faintly.
#. Repeat the following steps:
    a. Use the accelerometer to detect a tilt and move the pixel.
    b. If all the pixels have been found then:
        #. Display the location of the hidden pixels as when as the visited pixels.
        #. Scroll the score.
        #. Set up the game object again and play again.

| The code uses the class, ``TiltPixels()``, for the game object.
| 4 methods will be used below in the running of the code.

#. ``.tilt()`` will move a bright pixel in the direction of tilt.
#. ``.filled()`` will check if the hidden pixels have all been visited at by tilting.
#. ``.answer()`` will display the originally hidden pixels brightly and the other chosen pixels dimly.
#. ``.score()`` will calculate the score.


.. code-block:: python

    from microbit import *


    gamepix = TiltPixels()
    while True:
        gamepix.tilt()
        sleep(200)
        if gamepix.filled():
            gamepix.answer()
            display.scroll(gamepix.score())
            gamepix = TiltPixels()

----

The TiltPixels class
------------------------

.. admonition:: Tip
    
    **TiltPixels** is written in camel case. This is the python naming convention for classes. Each word is capitalized and their are no underscores. This is different to the convention for a variable which would be of the form **tilt_pixels**.


| Use a class for the game object since it makes it easy to group together the game data (attributes are variables belonging to a class)and game functions (methods are functions associated with a class).

.. py:class:: TiltPixels(x_position=random.randint(0, 4), y_position=random.randint(0, 4))

    | Set up the game object to control the pixels displayed and keep track of them.
    | The starting pixel is (x_position, y_position).
    | ``x_position`` and  ``y_position`` are optional. They are both integers from 0 to 4.
    | ``x_position`` by default will be a random integer from 0 to 4.
    | ``y_position`` by default will be a random integer from 0 to 4.

| The code below imports the random module and creates the game object by creating an instance of the TiltPixels class.

.. code-block:: python

    from microbit import *
    import random


    gamepix = TiltPixels()

----

