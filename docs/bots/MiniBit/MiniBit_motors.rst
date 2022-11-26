====================================================
MiniBit motors
====================================================

Pins for the motors are below.

=======  ===========================
 Pin     Purpose
=======  ===========================
 pin12   Left Motor
 pin8    Left Motor Backward

 pin14   Right Motor
 pin16   Right Motor Backward
=======  ===========================

----

Motor pin constants
----------------------------------------

| Set constants for the 4 motor pins to make the code more readable.
| e.g. left motor forward ``LMF = pin12``


.. admonition:: Tasks

    #. Set 4 constants for teh 4 motor pins.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Set 4 constants for teh 4 motor pins.

                    .. code-block:: python

                        from microbit import *

                        LMF = pin12
                        LMB = pin8
                        RMF = pin16
                        RMB = pin14
                        

----

Stop
----------------------------------------

| Use ``write_digital(0)`` to stop the motor controlled by each pin.

.. code-block:: python

    from microbit import *

    LMF = pin12
    LMB = pin8
    RMF = pin16
    RMB = pin14

    def stop():
        LMF.write_digital(0)
        LMB.write_digital(0)
        RMF.write_digital(0)
        RMB.write_digital(0)


----

Drive forwards
----------------------------------------

| Set constants for the 4 motor pins to make the code more readable.
| e.g. left motor forward ``LMF = pin12``
| Use a default parameter for speed at a low settings: ``def forwards(speed=200)``.
| Use ``write_analog(speed)`` to drive the motor where speed is from 0 to 1023.
| Use ``write_digital(0)`` to stop the other motors.
| If the motor drive forwards, the backward pin should be send ``write_digital(0)`` to turn it off.


.. code-block:: python

    from microbit import *

    LMF = pin12
    LMB = pin8
    RMF = pin16
    RMB = pin14

    def forwards(speed=200):
        LMF.write_analog(speed)
        LMB.write_digital(0)
        RMF.write_analog(speed)
        RMB.write_digital(0)

    forwards(200)

----

Drive forwards
----------------------------------------

| Set constants for the 4 motor pins to make the code more readable.
| e.g. left motor forward ``LMF = pin12``
| Use a default parameter for speed at a low settings: ``def mb_forwards(mb_speed=200)``.
| Use ``write_analog(speed)`` to drive the motor where speed is from 0 to 1023.
| Use ``write_digital(0)write_digital(0)`` to stop the motor.
| If the motor drive forwards, the backward pin should be send ``write_digital(0)`` to turn it off.


.. code-block:: python

    from microbit import *

    LMF = pin12
    LMB = pin8
    RMF = pin16
    RMB = pin14

    def forwards(speed=200):
        LMF.write_analog(speed)    # left forward
        LMB.write_digital(0)    # left backward
        RMF.write_analog(speed)    # right forward
        RMB.write_digital(0)    # right backward

    forwards(200)