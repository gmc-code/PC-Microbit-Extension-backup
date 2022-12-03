====================================================
Polygon Class
====================================================
    
| Write a **Polygon** class.
| Set the Polygon's **sides** on calling the Polygon class.
| Use Packing of positional arguments into a tuple when there are an arbitrary number of arguments.
| Use ``def __init__(self, *sides)`` to pack the arguments.
| e.g. ``tri1 = Polygon(3, 4, 5)``
| e.g. ``rect1 = Polygon(6, 8, 6, 8)``

| Write a method to return the perimeter of a polygon.
| Write code to ouput:
| tri1 with sides (3, 4, 5), has a perimeter of 12.
| rect1 with sides (6, 8, 6, 8), has a perimeter of 28.

.. admonition:: Tasks

    #. Write a **Polygon** class using the scaffold below.

        .. code-block:: python

            class Polygon:
                """A model of a Polygon."""

                def __init__(self, *sides):
                    self.sides = sides

                def perimeter(self):
                    return sum(           )

            tri1 = Polygon( 3, 4, 5)
            print(f'tri1 with sides {      }, has a perimeter of {            }.')
            rect1 = Polygon( 6, 8, 6, 8)
            print(f'rect1 with sides {      }, has a perimeter of {            }.')

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a Polygon class.

                .. code-block:: python

                    class Polygon:
                        """A model of a Polygon."""

                        def __init__(self, *sides):
                            self.sides = sides

                        def perimeter(self):
                            return sum(self.sides)

                    tri1 = Polygon(3, 4, 5)
                    print(f'tri1 with sides {tri1.sides}, has a perimeter of {tri1.perimeter()}.')
                    rect1 = Polygon(6, 8, 6, 8)
                    print(f'rect1 with sides {rect1.sides}, has a perimeter of {rect1.perimeter()}.')

