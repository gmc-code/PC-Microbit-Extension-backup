====================================================
Instance variables
====================================================

Variables unique to the instance
--------------------------------------

| Instance variables are variables, created in a class, that are unique to the instance.
| The __init__() function assigns values to instance variables when the object is created. e.g. ``self.game_level = 1``
| ``self.game_level`` is an instance variable. It is referenced using the self keyword.

.. code-block:: python

    class LevelGame:
        def __init__(self):
            self.game_level = 1

    game = LevelGame()
    print(game.game_level)

----

Instantiating a class instance with arguments
---------------------------------------------------

| Parameters can be used in the ``__init__`` definition so that arguments can be passed when the object is instantiated.
| e.g. the ``level`` parameter has been used in ``__init__(self, level)``.
| When game is instantiated using ``game = LevelGame(1)``, a value of 1 is passed in as the argument, so that ``level`` = 1.

.. code-block:: python

    class LevelGame:
        def __init__(self, level):
            self.game_level = level

    game = LevelGame(1)
    print(game.game_level)

----

Customary variable names
---------------------------------------------------

| Is it customary to use the same name for the parameters as for the instance variables.
| e.g. ``self.game_level = game_level``
| In the code above, a different variable name, ``level``, has been used instead of ``game_level`` to help see what is happening with the variables.
| The code below follows the custom.

.. code-block:: python

    class LevelGame:
        def __init__(self, game_level):
            self.game_level = game_level

    game = LevelGame(1)
    print(game.game_level)

----

.. admonition:: Tasks

    #. Run the code above and check the print output is 1.
    #. Modify the code to use ``game = LevelGame(2)`` and check the print output.

