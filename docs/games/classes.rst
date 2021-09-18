====================================================
Classes
====================================================

| See: https://www.w3schools.com/python/python_classes.asp

Objects
----------------------

| In Python, strings, integers, floats, lists, tuples, dictionaries etc. are objects, with their own data and methods.
| Every object has:
* a type
* data
* methods

| e.g  the object 'hello'
* type is str
* data is 'hello'
* methods are the standard string methods such a ``.title()`` and ``.lower()``.

| The defining of the standard string methods, while hiding how they are done, is called **abstraction**.
| Custom classes are a means of abstraction. They give the user ways to use data without having to worry about how the code works.

----

Classes and Objects
----------------------

| A Class is an object constructor, or a blueprint for creating objects.
| The name of the class is in camel case. e.g. **MicrobitGame**. Each word is capitalized and there are no underscores. 

| The code below creates a class, ``MicrobitGame``.
| The keyword **class** is followed by the name of the class then a colon. e.g. ``class MicrobitGame:``

| The class has a class variable, ``self.level``, and a class function, ``level_up()``.
| The __init__() function assigns values to object properties when the object is created. e.g. ``self.level = level``
| ``self.level`` is a class variable. Note that to access the class variable use the self keyword.
| ``def level_up(self):`` defines a class function. Note that the first parameter is self.

.. code-block:: python

    from microbit import *

    class MicrobitGame:
        def __init__(self, level):
            self.level = level

        def level_up(self):
            self.level += 1

----

Object instantiation
----------------------

| If classes are the blueprint for an object, then an object is what is made from the blueprint.

| Objects are an **encapsulation** of variables and functions. 
| Objects get their data attributes (properties) from class variables.
| Objects get their procedural attributes (methods) from class functions.

| The code below carries out object **instantiation** (making an instance).
| Objects are **instances** of classes.
| The object ``game`` is an the instance of the class ``MicrobitGame``. 
| The ``game`` instance is created below by calling the class and assigning the class to the variable ``game``.
| Now the variable "game" holds an object of the class "MicrobitGame" that contains the variable, level,  and the function, level_up,  defined within the class called "MicrobitGame".

.. code-block:: python

    game = MicrobitGame()

----

The __init__() function
--------------------------

| The __init__() function is used to assign values to object properties, or to do other operations that are necessary to do when the object is created.
| The __init__() function is called automatically every time the class is called to create a new object.
| The first parameter in the __init__() function is self, referring to the object itself.
| Other parameters can follow self.
| These other parameters are passed in as arguments when the class is called.
| e.g. ``game = MicrobitGame(level = 1)`` passes in ``level = 1`` to the __init__() function.
|  ``game = MicrobitGame(1)`` and ``game = MicrobitGame(level = 1)`` do the same thing.

.. code-block:: python

    from microbit import *

    class MicrobitGame:
        def __init__(self, level):
            self.level = level

        def level_up(self):
            self.level += 1

    game = MicrobitGame(level = 1)

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
| The **self** parameter is a reference to the current instance of the class.
| Methods in objects use the **self** parameter to reference the current instance of the class.

| It does not have to be named **self**, but it makes it easier for others if it is used, since that is what is expected.

----

Object Methods
----------------------

| In the code below, ``game.level_up()`` calls the method ``level_up`` to add one to the variable ``self.level`` 
| When calling the method on the game object, self is not written in the parentheses as it is automatically passed.
| The print statements output 1 then 2.

.. code-block:: python

    class MicrobitGame:
        def __init__(self, level):
            self.level = level

        def level_up(self):
            self.level += 1

    game = MicrobitGame(level = 1)
    print(game.level)
    game.level_up()
    print(game.level)

----

Object Methods with parameters
---------------------------------

| In the code below, ``game.set_speed(5)`` calls the method ``set_speed`` to set the variable ``self.speed`` to 5.
| The print statements output 1 then 5.

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



