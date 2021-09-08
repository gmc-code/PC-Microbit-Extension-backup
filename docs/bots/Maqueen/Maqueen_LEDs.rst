====================================================
Maqueen LEDs
====================================================

Set up  LEDs
----------------------------------------

| The maqueen buggy has 4 LEDs below the buggy.

.. py:class:: MaqueenNeoPixels() 

    | Set up the buggy's LEDs for use.
    | Use ``headlights = maqueen.MaqueenNeoPixels()`` to use the buggy's LEDs.

| The code below imports the maqueen module and sets up the LEDs.

.. code-block:: python

    from microbit import *
    import maqueen


    leds = maqueen.MaqueenNeoPixels()

----

MaqueenNeoPixels
----------------------------------------

| When setting up the LEDs, the colours of the front, indicator and rear LED settings are set to their default values.

.. py:class:: MaqueenNeoPixels(front=(20, 20, 20), indicator=(35, 25, 0), rear=(20, 0, 0))

    | ``front=(20, 20, 20)`` sets a low level white light.
    | ``indicator=(35, 25, 0)`` sets a low level yellow light.
    | ``rear=(20, 0, 0)`` sets a low level red light

----

Buggy lights and indicators
----------------------------------------

| There are four convenient methods that use the default LED settings:

.. py:method:: front_lights()

    | shows white at the front and red at the back.

.. py:method:: left_indicator()

    | shows yellow front left, white front right and red at the back.

.. py:method:: right_indicator()

    | shows yellow front right, white front left and red at the back

.. py:method:: both_indicators()

    | shows yellow at the front and red at the back.


| The code below shows white at the front and red at the back.

.. code-block:: python

    from microbit import *
    import maqueen


    leds = maqueen.MaqueenNeoPixels()

    leds.front_lights()

----

.. admonition:: Tasks

    #. Write code to alternate between both front LEDs being white and yellow. Use a 500ms sleep.
    #. Write code to blink the left indicator on and off each second.
    #. Write code to blink the right indicator on and off each second.
    #. Write code to alternate the left and right indicators each second.

----

Primary and secondary colours 
------------------------------

| Primary and secondary colours are shown below.
| The Red Green Blue (RGB) values for them are listed:
| white = (255, 255, 255)
| red = (255, 0, 0)
| yellow = (255, 255, 0)
| green = (0, 128, 0)
| cyan = (0, 255, 255)
| blue = (0, 0, 255)
| magenta = (255, 0, 255)

.. image:: images/primary_colours.png
    :scale: 50 %
    :align: left

.. image:: images/secondary_colours.png
    :scale: 50 %
    :align: center

----

Set buggy lights and indicators
----------------------------------------

| The default light settings can be altered.

.. py:method:: set_front(rgb=(20, 20, 20))

    | Set the front light LED colour to be used when ``front_lights()`` is used.
    | ``rgb`` is a tuple of 3 integers from 0 to 255, where 255 is full brightness.

| The code below sets the white lights at the front to full brightness.

.. code-block:: python

    from microbit import *
    import maqueen


    leds = maqueen.MaqueenNeoPixels()

    leds.set_front(rgb=(255, 255, 255))
    leds.front_lights()

----

.. admonition:: Tasks

    #. Write code to set the front LEDs to cyan. 
    #. Write code to set the front LEDs to blue. 

---- 

.. py:method:: set_indicator(rgb=(35, 25, 20))

    | Set the front light LED colour to be used when ``left_indicator()``, ``right_indicator()`` or ``both_indicators()`` are used.
    | ``rgb`` is a tuple of 3 integers from 0 to 255, where 255 is full brightness.

| The code below sets the indicator to yellow at the front to full brightness.

.. code-block:: python

    from microbit import *
    import maqueen


    leds = maqueen.MaqueenNeoPixels()

    leds.set_front(rgb=(255, 255, 0))
    leds.front_lights()

----

.. admonition:: Tasks

    #. Write code to set the indicator colour to magenta. 
    #. Write code to set the indicator colour to green. 

---- 

.. py:method:: set_rear(rgb=(20, 0, 0))

    | Set the rear light LED colour to be used when when ``front_lights()``, ``left_indicator()``, ``right_indicator()`` or ``both_indicators()`` are used.
    | ``rgb`` is a tuple of 3 integers from 0 to 255, where 255 is full brightness.

| The code below sets the red lights at the back to full brightness.

.. code-block:: python

    from microbit import *
    import maqueen


    leds = maqueen.MaqueenNeoPixels()

    leds.set_rear(rgb=(255, 0, 0))
    leds.front_lights()

----

.. admonition:: Tasks

    #. Write code to set the rear LEDs to green. 
    #. Write code to set the rear LEDs to blue. 

---- 

Set LEDs
----------------------------------------

| The default light settings can be altered.

.. py:method:: set_front(rgb=(20, 20, 20))

    | Set the front light LED colour to be used when ``front_lights()`` is used.
    | ``rgb`` is a tuple of 3 integers from 0 to 255, where 255 is full brightness.
