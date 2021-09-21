====================================================
Classes
====================================================

| The examples given are for use in python3 mode in Mu editor and are not microbit specific.
| See: https://www.w3schools.com/python/python_classes.asp

Objects
----------------------

| In Python, strings, integers, floats, lists, tuples, dictionaries etc. are objects, with their own data and methods.
| Every object has:
* a type
* data
* methods

| e.g  the string object 'hello'
* type is str
* data is 'hello'
* methods are the standard string methods such a ``.title()`` and ``.lower()``.

----

Classes and Objects
----------------------

| A Class is a code template, an object constructor, a blueprint for creating objects.

| The name of the class is in camel case. e.g. **LevelGame**. Each word is capitalized and there are no underscores. 

----

Creating a Class
----------------------

| The code below creates a class, ``LevelGame``.
| The keyword **class** is followed by the name of the class then a colon. e.g. ``class LevelGame:``
| ``pass`` is used as a placeholder for future code. When the pass statement is executed, nothing happens, but getting an error is avoided since empty code is not allowed in a class.

.. code-block:: python

    class LevelGame:
        pass

----

Object instantiation
----------------------

| An object is what is made from the class blueprint.
| Objects are **instances** of classes.
| The code below carries out object **instantiation** (making an instance).
| The ``game`` instance is created by calling the class, ``LevelGame()``, and assigning that to the variable ``game``.
| The object ``game`` is an instance of the class ``LevelGame``. 

.. code-block:: python

    class LevelGame:
        pass

    game = LevelGame()

----

Object data and methods
-----------------------------

| Variables and defintions can be gathered together in a class.
| Objects are an **encapsulation** of variables and functions. 
| Objects get their data attributes (properties) from class variables.
| Objects get their procedural attributes (methods) from class functions.

----

Class variables common to instances
------------------------------------------

| A class variable is shared by all instances of a class.
| ``game_level`` is a class variables.
| In the code below, both instances variables, ``game1.game_level`` and ``game2.game_level`` have the same value.

.. code-block:: python

    class LevelGame:
        game_level = 1

    game1 = LevelGame()
    print(game1.game_level)

    game2 = LevelGame()
    print(game2.game_level)

.. admonition:: Tasks

    #. Check that print output is the same for each statement above.
    #. Modify the code so that the class definition has a game_level of 2, then check its value for both instances.

----

Changing Class variables for all instances
----------------------------------------------

| A class variable can be altered in the class.
| In the code below, ``LevelGame.game_level = 3``, the class variable is changed to 3.
| The change in the class variable results in the same change for ``game1.game_level`` and ``game2.game_level``.

.. code-block:: python

    class LevelGame:
        game_level = 1

    game1 = LevelGame()
    game2 = LevelGame()

    LevelGame.game_level = 3
    print(game1.game_level)
    print(game2.game_level)

.. admonition:: Tasks

    #. Check that print output is the same for each statement above.
    #. Modify the code so that the LevelGame.game_level is set to 5, then check its value for both instances.

----

Changing Class variables in an instance
----------------------------------------------

| A class variable can be altered for a particular instance.
| ``game.game_level = 2`` changes the value of the variable within the instance.
| ``LevelGame.game_level`` is not altered.

.. code-block:: python

    class LevelGame:
        game_level = 1

    game = LevelGame()
    game.game_level = 2
    print(game.game_level)
    print(LevelGame.game_level)

.. admonition:: Tasks

    #. Check the print output to verify that the instance has a different value to the class.
    #. Add code after the instance value is changed so that the ``LevelGame.game_level`` is set to 5, then check the value for the instance to see if it is affected.

----

Instance variables
----------------------

| Instance variables are variables, created in a class, that are unique to the instance.
| The __init__() function assigns values to instance variables when the object is created. e.g. ``self.game_level = 1``
| ``self.game_level`` is an instance variable. It is referrenced using the self keyword.

.. code-block:: python

    class LevelGame:
        def __init__(self):
            self.game_level = 1

    game = LevelGame()
    print(game.game_level)


| Parameters can be used in the __init__ definition so that arguments can be passed when the object is instantiated.
| e.g the ``game_level`` parameter has been used in ``__init__(self, game_level)``.
| Is it customary to use the same name for the parameters as it is for the instance variables.
| e.g ``self.game_level = game_level``
| When game is instantiated using ``game = LevelGame(1)``, a value of 1 is passed in as the argument, so that game_level = 1.

.. code-block:: python

    class LevelGame:
        def __init__(self, game_level):
            self.game_level = game_level

    game = LevelGame(1)
    print(game.game_level)

.. admonition:: Tasks

    #. Run the code above and check the print output is 1.
    #. Use ``game = LevelGame(2)`` and check the print output.

----

The __init__() function
--------------------------

| The __init__() function is a built-in-function that is used to assign values to object properties, and to do other operations that are necessary to do when the object is created.
| The __init__() function is called automatically every time the class is called when creating a new object.
| The first parameter in the __init__() function is self, referring to the object itself.
| Other parameters can follow self. e.g ``__init__(self, game_level)``
| These other parameters, such as ``level``, are passed in as arguments when the class is called.
| e.g. ``game = LevelGame(game_level = 1)`` passes in ``game_level = 1`` to the __init__() function.
|  ``game = LevelGame(1)`` and ``game = LevelGame(game_level = 1)`` do the same thing.

| In the sample code, 2 instance variables are created.

.. code-block:: python

    from microbit import *

    class LevelGame:
        def __init__(self, game_level, player_lives):
            self.game_level = game_level
            self.player_lives = player_lives

    game = LevelGame(game_level=1, player_lives=3)


.. admonition:: Tasks

    #. Modify the code so that the game level starts at 0 with 5 lives.
    #. Modify the code by adding a third instance variable called level_score and initialize it to 0.

----

Self in variables
----------------------

| The **self** parameter is used to access variables that belong to the class.
| The dot . operator is then used to access the object variable.

----

Self in methods
----------------------

| Class functions use the **self** parameter (first parameter) to reference the current instance of the class.
| It does not have to be named **self**, but it makes it easier for others if it is used, since that is what is expected.

----

Object Methods
----------------------

| In the code below, ``game.game_level_up()`` calls the method ``level_up``.
| When calling the method on the game object, self is not written in the parentheses as it is automatically passed.
| The first print statement outputs 1, since it is instantiated with a level of 1.
| Then the second print statement outputs 2 after the ``level_up()`` method has been called.

| In the code below

.. code-block:: python

    class LevelGame:
        def __init__(self, game_level):
            self.game_level = game_level

        def level_up(self):
            self.game_level += 1

    game = LevelGame(game_level = 1)
    print(game.game_level)
    game.game_level_up()
    print(game.game_level)

.. admonition:: Tasks

    #. Check that print output is the same for each statement above.
    #. Modify the code so that the LevelGame.game_level is set to 5, then check its value for both instances.

----

Object Methods with parameters
---------------------------------

| In the code below, ``game.set_speed(5)`` calls the method ``set_speed`` to set the variable ``self.speed`` to 5.
| ``game = SpeedGame(1)`` sets the game speed to 1.
| The print statement outputs 1.
| ``game.set_speed(5)`` sets the game speed to 5.
| The print statement outputs 5.

.. code-block:: python

    class SpeedGame:
        def __init__(self, speed):
            self.speed = speed

        def set_speed(self, speed):
            self.speed = speed

    game = SpeedGame(1)
    print(game.speed)
    game.set_speed(5)
    print(game.speed)

.. admonition:: Tasks

    #. Check that print output is the same for each statement above.
    #. Modify the code so that the LevelGame.game_level is set to 5, then check its value for both instances.

----

Class variables
---------------------------------

| In the code below, ``game_number`` is a class variable.
| ``LevelGame.game_number += 1`` is used to increment the game number by 1 each time a the LevelGame is instantiated.
| Since ``game_number`` is a class variable, it is accessed within the class functions via ``LevelGame.game_number``. The **class name**,  ``LevelGame`` is used instead of **self**.


.. code-block:: python

    class LevelGame:
        game_number = 0
        
        def __init__(self, level):
            self.game_level = level
            LevelGame.game_number += 1
            
        def increase_level(self):
            self.game_level += 1

    game = LevelGame(1)
    print(game.game_level, game.game_number)
    game2 = LevelGame(2)
    print(game2.game_level, game2.game_number)


.. admonition:: Tasks

    #. Check that print output is the same for each statement above.
    #. Modify the code so that the LevelGame.game_level is set to 5, then check its value for both instances.

----
