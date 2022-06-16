====================================================
Games introduction
====================================================

| Some of the games in this section use python classes where convenient.

----

All time records
----------------

.. list-table::
    :widths: 60 20 60
    :header-rows: 1

    *   - **Game** 
        - **High score**  
        - **Player**
    *   - Asteroids
        - 1976    
        - Kevin
    *   - Falling Blocks
        - 154    
        - Sai
    *   - Space Invaders    
        - 365    
        - Snehath
    *   - Snake    
        - 11 
        - GMC




----

Game loop
---------------

| There are convenient ways to show to the user that the game can be played and played again.
| In the code below, an arrow pointing to the A button suggests to the user that they should press the A button.

.. code-block:: python
    
    
    from microbit import *


    while True:
        display.show(Image.ARROW_W)
        if button_a.is_pressed():
            PlayGame()
        sleep(1000)


----

| In the code below, when the game ends, "A or B" is scrolled across the screen and the user has 2 seconds to hold down the A or B buttons to play the game again, otherwise the ``while True`` loop is exited and the game can no longer be played.

.. code-block:: python
    
    
    from microbit import *


    while True:
        PlayGame()
        display.scroll("A or B", delay=80)
        sleep(2000)
        if button_a.is_pressed() or button_b.is_pressed():
            continue
        else:
            break

