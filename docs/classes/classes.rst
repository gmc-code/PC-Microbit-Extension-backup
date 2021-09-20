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

| The defining of the standard string methods, while hiding how they are done, is called **abstraction**.
| Custom classes are a means of abstraction. They give the user ways to use data without having to worry about how the code works.

----

Classes and Objects
----------------------

| A Class is a code template, an object constructor, or a blueprint for creating objects.

| The name of the class is in camel case. e.g. **LevelGame**. Each word is capitalized and there are no underscores. 

| The code below creates a class, ``LevelGame``.
| The keyword **class** is followed by the name of the class then a colon. e.g. ``class LevelGame:``
| ``pass`` is used as a placeholder for future code. When the pass statement is executed, nothing happens, but getting an error is avoided since empty code is not allowed in a class.

.. code-block:: python

    class LevelGame:
        pass

----

Object instantiation
----------------------

| If classes are the blueprint for an object, then an object is what is made from the blueprint.
| Objects are **instances** of classes.
| The code below carries out object **instantiation** (making an instance).
| The ``game`` instance is created by calling the class and assigning the class to the variable ``game``.
| The object ``game`` is an instance of the class ``LevelGame``. 

.. code-block:: python

    class LevelGame:
        pass

    game = LevelGame()

----

Classes variables
----------------------

| A class variable is shared by all instances of a class.
| ``game_name`` and ``game_level`` are class variables.

.. code-block:: python

    class LevelGame:
        game_name = 'levels'
        game_level = 1

    game = LevelGame()
    print(game.game_name)
    print(game.game_level)

----

Instance variables
----------------------

| The __init__() function assigns values to instance variables when the object is created. e.g. ``self.level = 1``
| ``self.level`` is an instance variable. It is referrenced using the self keyword.

.. code-block:: python

    class LevelGame:
        def __init__(self):
            self.level = 1

    game = LevelGame()
    print(game.level)



| ``self.level`` is an instance variable. It is referrenced using the self keyword.

.. code-block:: python

    class LevelGame:
        def __init__(self, level):
            self.level = level

    game = LevelGame(1)
    print(game.level)

----

Object instantiation
----------------------

| If classes are the blueprint for an object, then an object is what is made from the blueprint.

| Objects are an **encapsulation** of variables and functions. 
| Objects get their data attributes (properties) from class variables.
| Objects get their procedural attributes (methods) from class functions.

| The code below carries out object **instantiation** (making an instance).

.. code-block:: python

    game = LevelGame()

| Objects are **instances** of classes.
| The object ``game`` is an the instance of the class ``LevelGame``. 
| The ``game`` instance is created below by calling the class and assigning the class to the variable ``game``.
| Now the variable "game" holds an object of the class "LevelGame" that contains the variable, ``level``,  and the function, ``level_up``,  that were defined within the class called "LevelGame".

----

The __init__() function
--------------------------

| The __init__() function is a built in function that is used to assign values to object properties, or to do other operations that are necessary to do when the object is created.
| The __init__() function is called automatically every time the class is called when creating a new object.
| The first parameter in the __init__() function is self, referring to the object itself.
| Other parameters can follow self. e.g ``__init__(self, level)``
| These other parameters, such as ``level``, are passed in as arguments when the class is called.
| e.g. ``game = LevelGame(level = 1)`` passes in ``level = 1`` to the __init__() function.
|  ``game = LevelGame(1)`` and ``game = LevelGame(level = 1)`` do the same thing.

.. code-block:: python

    from microbit import *

    class LevelGame:
        def __init__(self, level):
            self.level = level

        def level_up(self):
            self.level += 1

    game = LevelGame(level = 1)

----

Self in variables
----------------------

| In the ``level_up`` function, ``self.level += 1`` has ``self.`` before the variable ``level``.
| The **self** parameter is used to access variables that belong to the class.
| The dot . operator is then used to access the object variable.

----

Self in methods
----------------------

| In the ``level_up`` function, ``def level_up(self):`` has self passed in as the current instance of the class.
| Methods in objects use the **self** parameter to reference the current instance of the class.

| It does not have to be named **self**, but it makes it easier for others if it is used, since that is what is expected.

----

Object Methods
----------------------

| In the code below, ``game.level_up()`` calls the method ``level_up``.
| When calling the method on the game object, self is not written in the parentheses as it is automatically passed.
| The first print statement outputs 1, since it is instantiated with a level of 1.
| Then the second print statement outputs 2 after the ``level_up()`` method has been called.

| In the code below

.. code-block:: python

    class LevelGame:
        def __init__(self, level):
            self.level = level

        def level_up(self):
            self.level += 1

    game = LevelGame(level = 1)
    print(game.level)
    game.level_up()
    print(game.level)

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
            self.level = level
            LevelGame.game_number += 1
            
        def increase_level(self):
            self.level += 1

    game = LevelGame(1)
    print(game.level, game.game_number)
    game2 = LevelGame(2)
    print(game2.level, game2.game_number)



