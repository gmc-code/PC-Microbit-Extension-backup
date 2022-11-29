====================================================
Creating a Class
====================================================

Class Creation
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
| Classes are an **encapsulation** of variables and functions. 
| Classes get their data attributes (properties) from variables within the class.
| Classes get their procedural attributes (methods) from functions within the class.

