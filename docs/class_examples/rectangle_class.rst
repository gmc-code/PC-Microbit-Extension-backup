====================================================
Rectangle Class
====================================================
    
| Write a **Rectangle** class.
| Set the rectangle's **width** and **length** on calling the Rectangle class.
| e.g. ``rect1 = Rectangle(6, 8)``

| Write 2 methods to return the perimeter and the area: 
| **perimeter**(), **area**()

| Write code to ouput:
| Milo is 2 years old.
| Milo rolled over!
| Milo is sitting.
| Daisy is 4 years old.
| Daisy ran after the ball.

.. admonition:: Tasks

    #. Write a **Rectangle** class using the scaffold below.

        .. code-block:: python

            class Dog:

                def __init__(self, name, age):
                    self.
                    self.
                    
                def get_info(self):
                    print(f"{          } is {           } years old.")

                def sit(self):
                    print(f"{       } is sitting.")

                def roll_over(self):
                    print(f"{          } rolled over!")

                def chase_ball(self):
                    print(f"{          } ran after the ball.")

                # instantiate 2 dogs
                his_dog = Dog('Milo', 2)
                his_dog.get_info()
                his_dog.roll_over()
                his_dog.sit()

                her_dog = Dog('Daisy', 4)
                her_dog.get_info()
                her_dog.chase_ball()

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a class for a dog.

                .. code-block:: python

                    class Dog:

                        def __init__(self, name, age):
                            self.name = name
                            self.age = age
                            
                        def get_info(self):
                            print(f"{self.name} is {self.age} years old.")

                        def sit(self):
                            print(f"{self.name} is sitting.")

                        def roll_over(self):
                            print(f"{self.name} rolled over!")

                        def chase_ball(self):
                            print(f"{self.name} ran after the ball.")


                    # instantiate 2 dogs
                    his_dog = Dog('Milo', 2)
                    his_dog.get_info()
                    his_dog.roll_over()
                    his_dog.sit()

                    her_dog = Dog('Daisy', 4)
                    her_dog.get_info()
                    her_dog.chase_ball()




