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

.. image:: images/encapsulation.png
    :scale: 50 %
    :align: center
    :alt: encapsulation

| Variables and definitions can be gathered together in a class.
| Objects are an **encapsulation** of variables and functions. 
| Objects get their data attributes (properties) from class variables.
| Objects get their procedural attributes (methods) from class functions.

----

Class variables common to instances
------------------------------------------

| A class variable is shared by all instances of a class.
| ``game_level`` is a class variable.
| In the code below, both instances variables, ``game1.game_level`` and ``game2.game_level`` have the same value.

.. code-block:: python

    class LevelGame:
        game_level = 1

    game1 = LevelGame()
    print(game1.game_level)

    game2 = LevelGame()
    print(game2.game_level)

.. admonition:: Tasks

    #. Check that the print output is the same for each print statement above.
    #. Modify the code so that the class definition has a game_level of 2, then check its value for both instances.

----

Changing Class variables for all instances
----------------------------------------------

| A class variable can be altered in the class.
| In the code below, ``LevelGame.game_level = 3``, the class variable is changed to 3.
| The change in the class variable results in the same change for the instance values of ``game1.game_level`` and ``game2.game_level``.

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
| ``self.game_level`` is an instance variable. It is referenced using the self keyword.

.. code-block:: python

    class LevelGame:
        def __init__(self):
            self.game_level = 1

    game = LevelGame()
    print(game.game_level)


| Parameters can be used in the ``__init__`` definition so that arguments can be passed when the object is instantiated.
| e.g the ``level`` parameter has been used in ``__init__(self, level)``.
| When game is instantiated using ``game = LevelGame(1)``, a value of 1 is passed in as the argument, so that ``level`` = 1.

.. code-block:: python

    class LevelGame:
        def __init__(self, level):
            self.game_level = level

    game = LevelGame(1)
    print(game.game_level)

| Is it customary to use the same name for the parameters as it is for the instance variables.
| e.g ``self.game_level = game_level``
| In the code above, a different variable name, ``level``, has been used instead of ``game_level`` to help see what is happening with the variables.

.. admonition:: Tasks

    #. Run the code above and check the print output is 1.
    #. Use ``game = LevelGame(2)`` and check the print output.

----

The __init__() function
--------------------------

| The ``__init__()`` function is a built-in-function that is used to assign values to object properties, and to do other operations that are necessary to do when the object is created.
| The ``__init__()`` function is called automatically every time the class is called when creating a new object.
| The first parameter in the ``__init__()`` function is self, referring to the object itself.
| Other parameters can follow self. e.g ``__init__(self, level)``
| These other parameters, such as ``level``, are passed in as arguments when the class is called.
| e.g. ``game = LevelGame(level = 1)`` passes in ``level = 1`` to the ``__init__()`` function.
|  ``game = LevelGame(1)`` and ``game = LevelGame(level = 1)`` do the same thing.
| e.g. ``game = LevelGame(level=1, lives=3)`` passes in ``level = 1`` and ``lives=3`` to the ``__init__()`` function.

| In the sample code, 2 instance variables are created.

.. code-block:: python

    from microbit import *

    class LevelGame:
        def __init__(self, level, lives):
            self.game_level = level
            self.player_lives = lives

    game = LevelGame(level=1, lives=3)


.. admonition:: Tasks

    #. Modify the code so that the game level starts at 0 with 5 lives.
    #. Modify the code so the parameters and the instance variables have matching names.
    #. Modify the code by adding a third instance variable using a parameter called level_score and initialize it to 0.

----

Self in variables
----------------------

| The **self** parameter is used to access variables that belong to the class as instance variables.
| The dot . operator is then used to access the object variable.
| e.g ``self.game_level``

----

Self in methods
----------------------

| Class functions use the **self** parameter (first parameter) to reference the current instance of the class.
| It does not have to be named **self**, but it makes it easier for others if it is used, since that is what is expected.

----

Regular Methods
----------------------

| In the code below, ``game.level_up()`` calls the method ``level_up``.
| ``self.game_level += 1`` adds 1 to ``self.game_level``.
| When calling the method on the game object, self is not written in the parentheses since it is automatically passed.
| The first print statement outputs 1, since the game object is instantiated with a game_level of 1.
| Then, after the ``level_up()`` method has been called, the second print statement outputs 2.

| In the code below

.. code-block:: python

    class LevelGame:
        def __init__(self, game_level):
            self.game_level = game_level

        def level_up(self):
            self.game_level += 1

    game = LevelGame(game_level = 1)
    print(game.game_level)

    game.level_up()
    print(game.game_level)


.. admonition:: Tasks

    #. Check that print output above is 1, then 2.
    #. Modify the level_up function in the previous example so that the level can't go above 10. Hint: use the max function.
    #. Modify the code so that the LevelGame.game_level starts at 10 then goes down by 1 when a level_down function is called.
    #. Modify the level_down function in the previous example so that the level can't go below 0. Hint: use the min function.

----

Regular Methods with parameters
-------------------------------------

| In the code below, ``game.set_speed(5)`` calls the method ``set_speed`` to set the variable ``self.game_speed`` to 5.
| ``game = SpeedGame(1)`` sets the game speed to 1.
| The print statement outputs 1.
| ``game.set_speed(5)`` sets the game speed to 5.
| The print statement outputs 5.

.. code-block:: python

    class SpeedGame:
        def __init__(self, game_speed):
            self.game_speed = game_speed

        def set_speed(self, game_speed):
            self.game_speed = game_speed

    game = SpeedGame(1)
    print(game.game_speed)

    game.set_speed(5)
    print(game.game_speed)


.. admonition:: Tasks

    #. Modify the set_speed function so that any speed values passed in are limited to a maximum speed of 10. Hint: use the max function.
    #. Modify the set_speed function so the speed must be between 0 and 10. Hint: use the min and max functions.

----

Modifying Class variables during instantiation
-------------------------------------------------

| In the code below, ``game_number`` is a class variable.
| ``LevelGame.game_number += 1`` is used to increment the game number by 1 each time a new LevelGame is instantiated.
| Since ``game_number`` is a class variable, it is accessed via ``LevelGame.game_number`` within the __init__ function. The **class name**,  ``LevelGame`` is used instead of **self**.


.. code-block:: python

    class LevelGame:
        game_number = 0
        
        def __init__(self, game_level):
            self.game_level = game_level
            LevelGame.game_number += 1

    game = LevelGame(1)
    game2 = LevelGame(2)

    print(game.game_number)
    print(game2.game_number)


.. admonition:: Tasks

    #. Check that print output shows that the class variable is the same for both instances.
    #. Add a third instance, game3, then check the class variable value for all three instances.

----

Class methods
-------------------------------------------------

| Class methods use the **cls** parameter as the first parameter for passing the class.
| In the code below, ``game_number`` is a class variable.
| The ``set_game_number`` function takes **cls** as the first parameter, and has ``game_number`` as a second parameter.
| The class variable, ``cls.game_number``, is set to the value of ``game_number``.
| The function is preceded by the decorator, ``@classmethod``, which is required to make the function work as a class method, so the function acts on the class rather than an instance of the class.
| The class method is called on the class using ``LevelGame.set_game_number(1)`` which sets the class variable, ``game_number``, to 1. 
| The class method, ``set_game_number``,  can be called on an instance, ``game``,  such as, ``game.set_game_number(1)``. This works like calling on the class, but it makes more sense to call it on the class itself.


.. code-block:: python

    class LevelGame:
        game_number = 0
        
        def __init__(self, game_level):
            self.game_level = game_level
            
        @classmethod        
        def set_game_number(cls, game_number):
            cls.game_number = game_number

    game = LevelGame(1)
    LevelGame.set_game_number(1)
    print(game.game_number)

.. admonition:: Tasks

    #. Modify the code so that the ``game_number`` is set to 5, then check its value for the instance, ``game``.

----

Using a Class method in the __init__ function
-------------------------------------------------

| In the code below, the class method ``increase_lives`` is called by the __init__ function.
| It increases the class variable, ``lives``,  by 1.

.. code-block:: python

    class LevelGame:
        lives = 3
        
        def __init__(self, game_level):
            self.game_level = game_level
            self.increase_lives()
            
        @classmethod        
        def increase_lives(cls):
            cls.lives += 1
            
    game1 = LevelGame(1)
    print(game1.lives)

    game2 = LevelGame(2)
    print(game2.lives)

.. admonition:: Tasks

    #. Modify the code so that the ``lives`` starts at 1 for the first time that ``LevelGame`` is called, then ``increase_lives`` increases lives by 2 each time it is called.

----

Class methods as alternative constructors
-------------------------------------------------

| In the code below, the class method ``make_game`` provides an alternate constructor to that of just calling the class to create a new instance.
| ``game1 = LevelGame(game_level = 1)`` result in game_level = 1 and game_lives = 5
| ``game2 = LevelGame.make_game(game_level = 1, game_lives = 3)`` results in game_level = 1 and game_lives = 3
| The last line of code, ``return cls(game_level)``, calls the __init__ function to create the new instance.

.. code-block:: python

    class LevelGame:
        game_lives = 5
        
        def __init__(self, game_level):
            self.game_level = game_level
            
        @classmethod        
        def set_game_lives(cls, game_lives):
            cls.game_lives = game_lives
            
        @classmethod
        def make_game(cls, game_level, game_lives):
            cls.set_game_lives(game_lives)
            return cls(game_level)
            
            
    game1 = LevelGame(game_level = 1)   
    print(game1.game_level, game2.game_lives)

    game2 = LevelGame.make_game(game_level = 1, game_lives = 3)
    print(game2.game_level, game2.game_lives)

.. admonition:: Tasks

    #. Modify the code to create a game at level 10 with 2 lives.

----

Static methods
-------------------------------------------------

| Static methods do not pass anything automatically.
| Compare this to regular methods which pass **self** automatically.
| Compare this to class methods which pass the **class** automatically.
| Static methods behave like regular functions and are included in the class since they have some logical connection with it.
| Choose to use static methods when there are no references to instance variables or class variables within it.

| Static methods do not require a class instance to be created first.
| The simplified code below illustrates this:

.. code-block:: python

    class LevelGame:
        
        @staticmethod        
        def get_required_level_score(game_level):
            return game_level * 10

    score = LevelGame.get_required_level_score(game_level = 3)
    print(score)


| In the code below, when the game is instantiated at a particular game level, ``game = LevelGame(game_level = 1)``, it will use the static method, ``get_required_level_score``, and then print the a value for it. 

| ``def get_required_level_score(level):`` does not pass in **self** to the function. 
| The decorator, ``@staticmethod``, is needed to make the function not require self to be passed in.

.. code-block:: python

    class LevelGame:
        game_lives = 5
        
        def __init__(self, game_level):
            self.game_level = game_level
            print(self.get_required_level_score(self.game_level))
            
        @staticmethod        
        def get_required_level_score(level):
            return level * 10

    game = LevelGame(game_level = 1)


.. admonition:: Tasks

    #. Write a static method that calculates a level bonus score using the formula: bonus = level * 5. Test out the static method and show that it is working for 2 different game levels.

