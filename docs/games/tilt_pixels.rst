====================================================
TiltPixels
====================================================

Game design
--------------------

| Code a game to find hidden pixels on the display by titling the microbit.
| Use a class object for the games pixels.
| The (x,y) coordinates of each pixel are in the diagram below.

.. image:: images/microbit_coords.png
    :scale: 100 %
    :align: center
    :alt: coordinates


#. Set up the game object (initialize an instance of the class)
    a. Set between 2 and 10 random pixels to be found.
    #. Start from a random pixel and display it brightly then faintly.
#. Repeat the following steps:
    a. Use the accelerometer to detect a tilt and move the pixel.
    #. If all the pixels have been found then:
        #. Scroll the score.
        #. Set up the game object again.


| The code below is the uses the class, ``TiltPixels()``, for the game object.
| 4 methods are used below in the running of the code:
    #. ``.tilt()`` will move a bright pixel in the direction of tilt
    #. ``.filled()`` will compare the hidden pixels with those arrived at by tilting
    #. ``.answer()`` will display the hidden pixels brightly and the other chosen pixels dimly.
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

The TiltPixels class
------------------------

