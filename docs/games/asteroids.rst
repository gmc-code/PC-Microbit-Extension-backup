====================================================
Asteroids
====================================================


| Asteroids; based on http://www.multiwingspan.co.uk/micro.php?page=charlie
| The game involves moving a ship, shown on the bottom row of the matrix. 
| The other pixel represents an asteroid that is falling towards the ship. 
| The player moves the ship left or right by pressing the A & B buttons to avoid contact with the asteroid.

.. code-block:: python

   # Asteroids; based on http://www.multiwingspan.co.uk/micro.php?page=charlie2

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


    class Ship:
        def __init__(self, x, y):
            self.x = x
            self.y = y


    def DrawGame(ship, asteroid1, asteroid2, t):
        img = Image("00000:" * 5)
        img.set_pixel(ship.x, ship.y, 9)
        img.set_pixel(asteroid1.x, asteroid1.y, 5)
        img.set_pixel(asteroid2.x, asteroid2.y, 5)
        return img


    def PlayGame():
        display.clear()
        score = 0
        asteroid1 = Asteroid(random.randint(0, 4), 0)
        asteroid2 = Asteroid(random.randint(0, 4), 2)
        ship = Ship(2, 4)
        tick = 0
        pause_time = 150  # 75
        sleep(1000)
        playing = True
        while playing:
            if button_a.was_pressed() and ship.x != 0:
                ship.x = ship.x - 1
            elif button_b.was_pressed() and ship.x != 4:
                ship.x = ship.x + 1
            i = DrawGame(ship, asteroid1, asteroid2, tick)
            # update ticks
            tick += 1
            if tick == 3:
                tick = 0
                asteroid1.update()
                asteroid2.update()
                score += 1
                i = DrawGame(ship, asteroid1, asteroid2, tick)
            if asteroid1.y == 4:
                if ship.x == asteroid1.x:
                    playing = False
            if asteroid2.y == 4:
                if ship.x == asteroid2.x:
                    playing = False
            display.show(i)
            sleep(pause_time)
        display.scroll(str(score))
        sleep(2000)


    while True:
        display.show(Image.ARROW_W)
        if button_a.was_pressed():
            PlayGame()
        sleep(500)


----

.. admonition:: Tasks

    #. Add sounds.
    #. Add a flashy start and end animation.
    #. Modify the code to speed up the game as the score increases.
    #. Modify the code to use more asteroids as the score increases.
    #. Modify the code to use levels with a screen indicating the new level.
