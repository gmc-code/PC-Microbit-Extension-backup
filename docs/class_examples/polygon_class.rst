====================================================
Polygon Class
====================================================
    
| Write a **Polygon** class.
| Set the Polygon's **sides** on calling the Polygon class.
| e.g. ``rect1 = Polygon(6, 8, 6, 8)``

| Write 1 method to return the perimeter: 
| **perimeter**()

| Write code to ouput:
| rect1 with sides 6, 8, 6, 8, has perimeter of 28.

.. admonition:: Tasks

    #. Write a **Polygon** class using the scaffold below.

        .. code-block:: python

            class Polygon:
                """A model of a Polygon."""

                def __init__(self, *args):
                    self.sides = args

                def perimeter(self):
                    return sum(self.sides)


            rect1 = Polygon( 6, 8, 6, 8,)
            print(f'rect1 with sides 6, 8, 6, 8, has perimeter of {rect1.perimeter()}.')

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a class for a dog.

                .. code-block:: python

                    class Polygon:
                        """A model of a Polygon."""

                        def __init__(self, *args):
                            self.sides = args

                        def perimeter(self):
                            return sum(self.sides)

                        def count(self):
                            return len(self.sides)

                        def average(self):
                            return round(self.perimeter() / self.count(), 1)


                    shape = Polygon(7, 12, 13)
                    print(shape.count())
                    print(shape.average())
                    print(shape.perimeter())