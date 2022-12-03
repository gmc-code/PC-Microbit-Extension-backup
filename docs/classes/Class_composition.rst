====================================================
Class Composition
====================================================

| See: https://www.geeksforgeeks.org/inheritance-and-composition-in-python/
| See: https://medium.com/swlh/the-best-way-to-understand-composition-in-python-5-case-studies-and-solution-4b23a6a2cc38

----

Composition
-----------------

| Composition models a has-a-relationship.
| Use composition to create components that can be reused by multiple classes.
| A composite class can be assigned to an instance variable.

----

Board Asteroid
-----------------

| In the code below, the composite class, Asteroid, is accessed via the self.asteroid1 and self.asteroid2 attribute of the Board class.

.. code-block:: python
        
    from microbit import *
    import random


    class Asteroid:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def update(self):
            self.y = self.y + 1
            if self.y == 5:
                self.y = 0
                self.x = random.randint(0, 4)


    class Board:
        def __init__(self):
            self.asteroid1 = Asteroid(random.randint(0, 4), 0)
            self.asteroid2 = Asteroid(random.randint(0, 4), 1)

        def draw_board(self):
            self.board = Image("00000:" * 5)
            self.board.set_pixel(self.asteroid1.x, self.asteroid1.y, 9)
            self.board.set_pixel(self.asteroid2.x, self.asteroid2.y, 9)
            display.show(self.board)

        def update_board(self):
            self.asteroid1.update()
            self.asteroid2.update()

    game_board = Board()
    game_board.draw_board()

    while True:
        sleep(300)
        game_board.update_board()
        game_board.draw_board()


----

Board Asteroid Ship
---------------------

| In the code below, the composite class, Ship has been added so that it is accessed via the self.ship attribute of the Board class.

.. code-block:: python
        
    from microbit import *
    import random

    class Asteroid:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def move(self):
            self.y = self.y + 1
            if self.y == 5:
                self.y = 0
                self.x = random.randint(0, 4)

    class Ship:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def move(self):
            if button_a.is_pressed() and self.x != 0:
                self.x = self.x - 1
            elif button_b.is_pressed() and self.x != 4:
                self.x = self.x + 1
                
    class Board:
        def __init__(self):
            self.ship = Ship(2, 4)
            self.asteroid1 = Asteroid(random.randint(0, 4), 0)
            self.asteroid2 = Asteroid(random.randint(0, 4), 1)

        def draw_board(self):
            self.board = Image("00000:" * 5)
            self.board.set_pixel(self.ship.x, self.ship.y, 9)
            self.board.set_pixel(self.asteroid1.x, self.asteroid1.y, 5)
            self.board.set_pixel(self.asteroid2.x, self.asteroid2.y, 5)
            display.show(self.board)

        def update_board(self):
            self.ship.move()
            self.asteroid1.move()
            self.asteroid2.move()

    game_board = Board()
    game_board.draw_board()

    while True:
        sleep(300)
        game_board.update_board()
        game_board.draw_board()