====================================================
Classes
====================================================

| See: https://www.w3schools.com/python/python_classes.asp

Objects
----------------------

| Almost everything in Python is an object, with its own attributes and methods.
| Every object has:
* a type
* data
* a set of procedures for interaction with the object

| an object is an instance of a type
    • 1234 is an instance of an int
    • "hello"is an instance of a string
    • 
objects are a data abstractionthat captures…
(1) an internal representation
•through data attributes
(2) an interfacefor interacting with object
•through methods (aka procedures/functions)
•defines behaviors but hides implementation

Classes and Objects
----------------------
| Objects are an **encapsulation** of variables and functions. 
| Objects get their attributes (properties) from class variables.
| Objects get their methods from class functions.

| A Class is like an object constructor, or a "blueprint" for creating objects.
| A class is created by the keyword class.
| The name of the class is in camel case. e.g. **MicrobitGame**. Each word is capitalized and there are no underscores. 

| The code below is a simple class.
| The class statement creates a new class definition. The keyword **class** is followed by the name of the class then a colon. e.g. ``class MicrobitGame:``
| The __init__() function assigns values to object properties when the object is created. 
| e.g. ``self.level = level``
| ``self.level`` is a class variable.
| ``increase_level(self)`` is a class function.


.. code-block:: python

    from microbit import *

    class MicrobitGame:
        def __init__(self, level):
            self.level = level

        def increase_level(self):
            self.level += 1



Object instantiation
----------------------

| The code below carries out object instantiation.
| The object ``game`` is an the instance of the class ``MicrobitGame``. 
| The ``game`` instance is created below by calling the class and assigning the class to a variable.

.. code-block:: python

    game = MicrobitGame():



| Methods in objects use the self parameter to reference the current instance of the class.
 and to access variables that belong to the class.

You will then be able to access the attributes that are present inside the class using the dot . operator. 
