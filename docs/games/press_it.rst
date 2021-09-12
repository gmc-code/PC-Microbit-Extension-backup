====================================================
Press It game
====================================================

Game design
--------------------

| Press It is a game to press the A or B button after 'A' or 'B' is shown.
| A class is used to run the game.

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



.. code-block:: python

    from microbit import *
    import random


    game = PressItGame()

----

The PressItGame class
------------------------

| Use a class for the game object since it makes it easy to group together the game data and game functions.

.. py:class:: PressItGame()

    | Set up the game object to control the game, including the hidden and visited pixels.
    | Initial x, y values for the initial pixel could be passed here as an argument.
    | ``gamepix = TiltPixels(2,2)`` would place the initial pixel in the center of the 5 by 5 grid.
    | There is no need to do so since the game has a constructor method to start at a random pixel.

| The code below imports the random module and creates the game object by creating an instance of the TiltPixels class.

.. code-block:: python

    from microbit import *
    import random


    game = PressItGame()


----

The TiltPixels constructor
---------------------------------

.. py:method:: __init__(x_position=random.randint(0, 4), y_position=random.randint(0, 4))

    | The __init__() method is the constructor called when the game object is created.
    | The starting pixel is at the coordinates: ``(x_position, y_position)``.
    | ``x_position`` is the starting x value which by default will be a random integer from 0 to 4.
    | ``y_position`` is the starting y value which by default will be a random integer from 0 to 4.

| ``self.x_position`` keeps track of the x position of the current pixel.
| ``self.y_position`` keeps track of the y position of the current pixel.
| ``self.pixels_filled`` is initialized as a set with the starting pixel tuple: ``(x_position, y_position)``. A set is used to make it easy to keep track of the visited pixels. A set is used instead of a list because sets don't allow duplicate values to be stored. When the microbit is tilted, each pixel will be added to the set. 
| ``self.pixels_to_get`` stores the set of hidden pixels created using ``pixels_to_get()``. 
| ``self.show()`` displays the pixel at (x_position, y_position).

| The __init__ method is given below.

.. code-block:: python

    class PressItGame:
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

    | Create a set of tuples of (x, y) coordinates for 2 to 10 hidden pixels.
    | e.g with 5 pixels: {(2, 1), (4, 1), (3, 4), (2, 0), (1, 1)}

| The decorator ``@staticmethod``, makes the function a static method. This utility function doesn't access any properties of the class. No reference to ``self`` is passed to it.


.. code-block:: python

    class PressItGame:
        ...

----

Game code
---------------------------------

| The game code is below.

.. code-block:: python

    """PressIt_game: Press the A or B button when the text is shown"""

    from microbit import *
    import random


    SPEED = {1: 1200, 2: 1000, 3: 800, 4: 700, 5: 600, 6: 550, 7: 500, 8: 450}
    LEVELUP = (3, 6, 9, 12, 15, 18, 21)
        
    class PressItGame():
            
        def __init__(self):
            self.level = 1
            self.score = 0
            
        def show_a(self):
            display.show("A")

        def show_b(self):
            display.show("B")

        def show_yes(self):
            display.show(Image.YES)
            sleep(500)
            
        def show_no(self):
            display.show(Image.NO)
            sleep(500)
            
        def show_levelup(self):
            display.show(Image.ARROW_N)
            display.scroll('level ' + str(self.level), delay=60)
            sleep(500)

        def is_correct_button(self):
            button_number = random.randint(0, 1)
            if button_number == 0:
                self.show_a()
            elif button_number == 1:
                self.show_b()  
            a_pressed = False
            b_pressed = False
            start_time= running_time()
            now = running_time()
            while now - start_time < SPEED[self.level]:
                if button_a.is_pressed():
                    a_pressed = True
                if button_b.is_pressed():
                    b_pressed = True
                now = running_time()
            if button_number == 0:
                if a_pressed is True and b_pressed is False:
                    return True
                else:
                    return False
            elif button_number == 1:
                if a_pressed is False and b_pressed is True:
                    return True
                else:
                    return False
                    
        def run_game(self):
            display.scroll("A or B")
            display.scroll('level ' + str(self.level), delay=60)
            gameover = False
            while gameover is False:
                if self.is_correct_button():
                    self.show_yes()
                    self.score += 1
                    if self.score in LEVELUP:
                        self.level += 1
                        self.show_levelup()
                else:
                    gameover = True
                    self.show_no()
                    display.scroll('score ' + str(self.score), delay=60)

    while True:
        if button_a.is_pressed() and button_b.is_pressed():
            break
        game = PressItGame()
        game.run_game()







----

.. admonition:: Tasks

    #. Modify the code to display left and right arrows instead of 'A' and 'B'.
    #. Add an animation of 3 to 6 built in image shapes when the level reaches level 5.
    #. Replace the level scrolled text with an animation in which the number of images in the animation is equal to the level number.
    #. Add code to store all the game scores and display the average score after each game.
    #. Add code to store the best game score after each game and display the best score after exiting by pressing both buttons.

