====================================================
Press It game
====================================================

Game design
--------------------

| Press It is a game to press the A or B button after 'A' or 'B' is shown.
| A class is used to run the game.

#. Set up the game object
    a. Assign values to the TIMELIMIT dictionary.
    b. Assign values to the LEVELUP tuple.
    c. Set the score to 0.
    d. Set the level to 1
#. Run the game:
    a. Show 'A' or 'B'.
    b. If the correct button is pressed within the time limit then:
        #. Display a tick (Image.YES)
        #. Add one to the score
        #. Level up if the next level has been reached.
    b. If the wrong button is pressed or no button is pressed within the time limit then:
        #. Display an X (Image.NO)
        #. Scroll the score

| The code uses the class, ``PressItGame()``, for the game object.
| 8 methods will be used.

#. ``.show_a()`` shows 'A' to direct the user to press the A button.
#. ``.show_b()`` shows 'B' to direct the user to press the B button.
#. ``.show_yes()`` displays a tick when the correct button is pressed.
#. ``.show_no()`` displays a cross when the wrong button is pressed.
#. ``.show_levelup()`` shows an up arrow then the level number.
#. ``.is_correct_button()`` waits according to the level TIMELIMIT and returns
#. ``.show_a()`` show 'A' to direct the user to press the A button.
#. ``.show_b()`` show 'B' to direct the user to press the B button.



.. code-block:: python

    from microbit import *
    import random


    game = PressItGame()

----

The PressItGame class
------------------------

| Use a class for the game object.

.. py:class:: PressItGame()

    | Set up the game object to control the game, including the SPEED dictionary, the LEVELUP tuple, the initial level and score.

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

Game code
---------------------------------

| The game code is below.

.. code-block:: python

    """PressIt_game: Press the A or B button when the text is shown"""

    from microbit import *
    import random


    class PressItGame():
        
        TIMELIMIT = {1: 1200, 2: 1000, 3: 800, 4: 700, 5: 600, 6: 550, 7: 500, 8: 450, 9: 400}
        LEVELUP = (3, 6, 9, 12, 15, 18, 21, 24)
        
        def __init__(self):
            self.score = 0
            self.level = 1

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
            while now - start_time < self.TIMELIMIT[self.level]:
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
            game_over = False
            while game_over is False:
                if self.is_correct_button():
                    self.show_yes()
                    self.score += 1
                    if self.score in self.LEVELUP:
                        self.level += 1
                        self.show_levelup()
                else:
                    game_over = True
                    self.show_no()
                    display.scroll('score ' + str(self.score), delay=60)

    game = PressItGame()
    game.run_game()
    if button_a.was_pressed() and button_b.was_pressed():
        sleep(100)
    while True:
        if button_a.was_pressed() and button_b.was_pressed():
            game = PressItGame()
            game.run_game()
        else:
            sleep(2000)







----

.. admonition:: Tasks

    #. Modify the code to display left and right arrows instead of 'A' and 'B'.
    #. Add an animation of 3 to 6 built in image shapes when the level reaches level 5.
    #. Replace the level scrolled text with an animation in which the number of images in the animation is equal to the level number.
    #. Add code to store all the game scores and display the average score after each game.
    #. Add code to store the best game score after each game and display the best score after exiting by pressing both buttons.

