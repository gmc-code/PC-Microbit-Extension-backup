====================================================
Classes
====================================================

| See: https://www.w3schools.com/python/python_classes.asp

Objects
----------------------

| Almost everything in Python is an object, with its own data attributes and methods.
| Every object has:
* a type
* data
* procedures

| e.g  the object 'hello'
* type is str
* data is 'hello'
* procedures include the standard string methods such a ``.title()`` and ``.lower()``.

| The defining of the standard string methods while hiding how they are done is called **abstraction**.
| Custom cClasses are a means of abstraction.

Classes and Objects
----------------------

| A Class is an object constructor, or a "blueprint" for creating objects.
| A class is created by the keyword **class**. e.g ``class MicrobitGame:``
| The name of the class is in camel case. e.g. **MicrobitGame**. Each word is capitalized and there are no underscores. 

| The code below creates a simple class.
| The class statement creates a new class definition. 
| The keyword **class** is followed by the name of the class then a colon. e.g. ``class MicrobitGame:``

| The __init__() function assigns values to object properties when the object is created. 
| e.g. ``self.level = level``
| ``self.level`` is a class variable. Note that to access the class attribute use the self keyword.
| ``def increase_level(self):`` defines a class function. Note that the first argument is self

.. code-block:: python

    from microbit import *

    class MicrobitGame:
        def __init__(self, level):
            self.level = level

        def increase_level(self):
            self.level += 1


Object instantiation
----------------------

| Objects are an **encapsulation** of variables and functions. 
| Objects get their data attributes (properties) from class variables.
| Objects get their procedural attributes (methods) from class functions.

| The code below carries out object **instantiation** (making an instance).
| Objects are **instances** of classes.
| The object ``game`` is an the instance of the class ``MicrobitGame``. 
| The ``game`` instance is created below by calling the class and assigning the class to the variable ``game``.

.. code-block:: python

    game = MicrobitGame()


Object Methods
----------------------

| Methods in objects use the self parameter to reference the current instance of the class.
| The dot . operator is then used to access the object variable.

.. code-block:: python

    from microbit import *

    class MicrobitGame:
        def __init__(self, level):
            self.level = level

        def increase_level(self):
            self.level += 1

    game = MicrobitGame(level = 1)

| The self parameter is used to access variables that belong to the class.


