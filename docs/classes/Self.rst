====================================================
Self
====================================================


Self in variables
----------------------

| The **self** parameter is used to access variables that belong to the class as instance variables.
| The dot, '.', operator is then used to access the object variable.
| e.g. ``self.game_level``

----

Self in methods
----------------------

| Class functions use the **self** parameter (first parameter) to reference the current instance of the class.
| It does not have to be named **self**, but it makes it easier for others if it is used, since that is common practice.

----

.. admonition:: Tasks

    #. Modify the code to use ``self`` where customary.

    .. code-block:: python

        class LevelGame:
            def __init__(game, game_level):
                game.game_level = game_level

