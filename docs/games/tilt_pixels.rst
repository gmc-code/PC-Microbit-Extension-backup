====================================================
TiltPixels
====================================================

| Code a game to find hidden pixels on the display by titling the microbit.
| Use a class object for the games pixels to be found and for those tried by tilting

.. image:: images/microbit_coords.png
    :scale: 100 %
    :align: center
    :alt: coordinates


#. Set up the game object (initialize an instance of the class)
#. Set between 2 and 10 random pixels to be found and put them in a set for comparison.
#. Start from a random pixel and display it brightly then faintly.
#. Add this starting pixel to a set that keeps track of where the pixel has moved on the display.
#. Repeat the following steps:
#. Use the accelerometer to detect a tilt and move the pixel a maximum of 1 position left or right and up or down according to the tilt.
#. Update the set of pixels the 


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