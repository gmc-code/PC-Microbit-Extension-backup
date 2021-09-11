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
| 4 methods will be used.

#. ``.tilt()`` will move a bright pixel in the direction of tilt.
#. ``.filled()`` will check if all the hidden pixels have been visited by tilting.
#. ``.answer()`` will display the hidden pixels brightly and the visited pixels dimly.
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
    
    **TiltPixels** is written in camel case. This is the python naming convention for classes. Each word is capitalized and their are no underscores. This is different to the convention for a variable which would be written in snake case as **tilt_pixels**.

| Use a class for the game object since it makes it easy to group together the game data and game functions.
| The game data is in attributes. Attributes are variables belonging to a class.
| The game functions are know as methods. Methods are functions associated with a class.


.. py:class:: TiltPixels()

    | Set up the game object to control the pixels displayed and keep track of them.

| The code below imports the random module and creates the game object by creating an instance of the TiltPixels class.

.. code-block:: python

    from microbit import *
    import random


    gamepix = TiltPixels()

----

The TiltPixels constructor
---------------------------------

.. py:method:: __init__(self, x_position=random.randint(0, 4), y_position=random.randint(0, 4))

| The __init__() method is the constructor called when the game object is created.
| The random starting pixel is ``(x_position, y_position)``.
| ``x_position`` is the starting x value which by default will be a random integer from 0 to 4.
| ``y_position`` is the starting y value which by default will be a random integer from 0 to 4.
| ``self.x_position`` keeps track of the current pixel x position.
| ``self.y_position`` keeps track of the current pixel y position.
| ``self.pixels_filled`` is initialized as a set with the the starting pixel tuple: ``(x_position, y_position)``. A set is used to make it easy to keep track of the visited pixels. A set is used instead of a list because sets don't allow duplicate values to be stored. When the microbit is tilted, each pixel will be added to the set. 
| ``self.pixels_to_get`` stores the set of hidden pixels. 

| The __init__ method is given below.

.. code-block:: python

    class TiltPixels:
        def __init__(self, x_position=random.randint(0, 4), y_position=random.randint(0, 4)):
            self.x_position = x_position
            self.y_position = y_position
            self.pixels_filled = set((x_position, y_position))
            self.pixels_to_get = self.pixels_to_get()
            self.show()



----

The hidden pixels
---------------------------------

| ``pixels = set()`` creates an empty set.
| ``pixels.add((x, y))`` adds a tuple of the x and y values to the set. These are the coordinates of each hidden pixel to find.
| ``for _ in range(random.randint(2, 10))`` controls the number of pixels to find. There will be from 2 to 10 pixels to find. ``_`` is used by convention when the iterator variable is not needed in the following code.


.. code-block:: python

    @staticmethod
    def pixels_to_get():
        pixels = set()
        for _ in range(random.randint(2, 10)):
            pixels.add((random.randint(0, 4), random.randint(0, 4)))
        return pixels
