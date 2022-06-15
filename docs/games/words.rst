====================================================
Words
====================================================


| Words based on based on http://www.multiwingspan.co.uk/micro.php?page=acctext
| Press A to start
| Tilt left or right to change letter.
| Press A to add the letter.
| Press B to finish the word and scroll it.




.. code-block:: python

    # based on http://www.multiwingspan.co.uk/micro.php?page=acctext
    from microbit import *


    # charset is a list of ASCII codes in our character set
    charset = [i for i in range(65, 91)]  # upper case letters
    # charset += [k for k in range(48, 58)]  # digits
    # charset += [l for l in range(32, 48)]  # punctuation and symbols

    # chars is a list of characters in our character set
    chars = [chr(i) for i in charset]
    maxchar = len(chars)


    def GetLetter():
        current = 12
        display.show(chars[current])
        while button_a.was_pressed() is False:
            if button_b.is_pressed():
                return ""
            if accelerometer.get_x() > 300:
                current += 1
            elif accelerometer.get_x() < -300:
                current -= 1
            current = max(0, min(current, maxchar - 1))
            display.show(chars[current])
            sleep(500)
        return chars[current]


    def GetString():
        usertext = ""
        while button_b.was_pressed() is False:
            usertext += GetLetter()
        return usertext


    while True:
        display.show(Image.ARROW_W)
        if button_a.is_pressed():
            display.clear()
            sleep(1000)
            a = button_a.was_pressed()
            currentWord = GetString()
            display.scroll(currentWord)
        sleep(500)





----

.. admonition:: Tasks

    #. Modify the code to use lower case letters.
    #. Modify the code to use numbers instead of letters.


