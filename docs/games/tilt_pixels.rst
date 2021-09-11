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
| The game data are attributes. Attributes are variables belonging to a class.
| The game functions are methods. Methods are functions associated with a class.


.. py:class:: TiltPixels()

    | Set up the game object to control the pixels displayed and keep track of them.
    | Initial x, y values for the initial pixel could be passed here.
    | ``gamepix = TiltPixels(2,2)`` would place the initial pixel in the center of the 5 by 5 grid.
    | There is no need to do so since the game will start at a random pixel.

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
| The starting pixel is at the coordinates: ``(x_position, y_position)``.
| ``x_position`` is the starting x value which by default will be a random integer from 0 to 4.
| ``y_position`` is the starting y value which by default will be a random integer from 0 to 4.
| ``self.x_position`` keeps track of the current pixel x position.
| ``self.y_position`` keeps track of the current pixel y position.
| ``self.pixels_filled`` is initialized as a set with the the starting pixel tuple: ``(x_position, y_position)``. A set is used to make it easy to keep track of the visited pixels. A set is used instead of a list because sets don't allow duplicate values to be stored. When the microbit is tilted, each pixel will be added to the set. 
| ``self.pixels_to_get`` stores the set of hidden pixels created using ``pixels_to_get()``. 
| ``self.show`` displays the pixel at (x_position, y_position).

| The __init__ method is given below in its class.

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

.. py:method:: pixels_to_get()

    | Create a set of tuples of x, y coordinates for 2 to 10 hidden pixels.

| ``pixels = set()`` creates an empty set.
| ``pixels.add((x, y))`` adds a tuple of the x and y values to the set. These are the coordinates of each hidden pixel to find.
| ``for _ in range(random.randint(2, 10))`` controls the number of pixels to find. There will be from 2 to 10 pixels to find. ``_`` is used by convention when the iterator variable is not needed in the for-loop body.
| The decorator ``@staticmethod``, makes the function a static method. This utility function doesn't access any properties of the class. No reference to ``self`` is passed to it.

.. code-block:: python

    class TiltPixels:
    ...
        @staticmethod
        def pixels_to_get():
            pixels = set()
            for _ in range(random.randint(2, 10)):
                pixels.add((random.randint(0, 4), random.randint(0, 4)))
            return pixels

----

Accelerometer
---------------------------------

.. py:method:: acc_x_change()

    | Return an integer that will be used to move the pixel left to right.
    | Values are: -1 to move to the left, 0 for no change and 1 to move to the right.
    | A sensitivity of 300 is exceeded with a small tilt.

.. code-block:: python


    class TiltPixels:
    ...

        def acc_x_change(self):
            sensitivity = 300
            accx = accelerometer.get_x()
            if accx < -sensitivity:
                xd = -1
            elif accx > sensitivity:
                xd = 1
            else:
                xd = 0
            return xd

----

.. py:method:: acc_y_change()

    | Return an integer that will be used to move the pixel left to right.
    | Values are: -1 to move to the left, 0 for no change and 1 to move to the right.
    | A sensitivity of 300 is exceeded with a small tilt.

.. code-block:: python


    class TiltPixels:
    ...

        def acc_y_change(self):
            sensitivity = 300
            accy = accelerometer.get_y()
            if accy < -sensitivity:
                yd = -1
            elif accy > sensitivity:
                yd = 1
            else:
                yd = 0
            return yd








----

.. admonition:: Tasks

    #. Modify the code to require a button press to continue with a new game.
    #. Write code to store all the game scores and display the average score with a button press.
    #. Write code to use the A and B buttons to adjust the tilt sensitivity in steps of about 100. Use both button being pressed to save the sensitivity and reuse it for new games.


