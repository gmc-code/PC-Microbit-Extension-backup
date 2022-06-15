====================================================
Asteroids
====================================================


| Asteroids; see http://www.multiwingspan.co.uk/micro.php?page=charlie

.. code-block:: python

    # Asteroids; see http://www.multiwingspan.co.uk/micro.php?page=charlie2

    from microbit import *
    import random

    class Asteroid():
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def update(self):
            self.y = self.y + 1
            if self.y==5:
                self.y=0
                self.x=random.randint(0,4)
    class Ship():
        def __init__(self, x, y):
            self.x = x
            self.y = y

    def DrawGame(t):
        img = Image('00000:'*5)
        img.set_pixel(ship.x, ship.y, 9)  #(t % 2)*9)
        img.set_pixel(asteroid1.x, asteroid1.y, 9)
        img.set_pixel(asteroid2.x, asteroid2.y, 9)
        return img

    while True:
            display.show(Image.ARROW_W)
            if button_a.was_pressed():
                display.clear()
                score = 0
                asteroid1 = Asteroid(random.randint(0,4),0)
                asteroid2 = Asteroid(random.randint(0,4),2)
                ship = Ship(2,4)
                tick = 0
                paws = 150  # 75
                sleep(1000)
                playing = True
                while playing:
                    if button_a.was_pressed() and ship.x!=0:
                        ship.x = ship.x - 1
                    elif button_b.was_pressed() and ship.x!=4:
                        ship.x = ship.x + 1
                    i = DrawGame(tick)
                    # update ticks
                    tick += 1
                    if tick == 3:
                        tick = 0
                        asteroid1.update()
                        asteroid2.update()
                        score += 1
                        i = DrawGame(tick)
                    if asteroid1.y==4:
                        if ship.x==asteroid1.x:
                            playing = False
                    if asteroid2.y==4:
                        if ship.x==asteroid2.x:
                            playing = False
                    display.show(i)
                    sleep(paws)
                display.scroll(str(score))
                sleep(2000)
            sleep(100)
