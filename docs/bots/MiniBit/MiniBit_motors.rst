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

| Set constants for the 4 motor pins.
| e.g. left motor forward ``LMF = pin12``


.. admonition:: Tasks

    #. Set constants for the 4 motor pins.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                .. code-block:: python

                    from microbit import *

                    LMF = pin12
                    LMB = pin8
                    RMF = pin16
                    RMB = pin14
                        

----

Stop
----------------------------------------

| Use ``write_digital(0)`` to stop the motors controlled by each pin.

.. admonition:: Tasks

    #. Write code to stop all motors in a def block: ``def stop()``.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

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

                    stop()

----

Drive forwards
----------------------------------------

| Drive the buggy forwards.
| Use a default speed as in ``def forwards(speed=200)``.
| Use ``write_analog(speed)`` to drive the motor where speed is from 0 to 1023.
| Use ``write_digital(0)`` to stop the other motors.
| If the motor drives forwards, the backwards pin should be sent ``write_digital(0)`` to turn it off.


.. admonition:: Tasks

    #. Write code to drive forwards using: ``def forwards(speed=200)``.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

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

                    forwards(speed=200)

----

Drive backwards
----------------------------------------

| Drive the buggy backwards.
| Use a default speed as in ``def backwards(speed=200)``.
| Use ``write_analog(speed)`` to drive the motor where speed is from 0 to 1023.
| Use ``write_digital(0)`` to stop the other motors.
| If the motor drives backwards, the forwards pin should be sent ``write_digital(0)`` to turn it off.


.. admonition:: Tasks

    #. Write code to drive backwards using: ``def backwards(speed=200)``.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                .. code-block:: python

                    from microbit import *

                    LMF = pin12
                    LMB = pin8
                    RMF = pin16
                    RMB = pin14

                    def backwards(speed=200):
                        LMF.write_digital(0)
                        LMB.write_analog(speed)
                        RMF.write_digital(0)
                        RMB.write_analog(speed)

                    backwards(speed=200)

