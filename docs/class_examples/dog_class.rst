====================================================
Dog Class
====================================================
    
| Set the dog's name and age on calling the Dog class.
| Call the dog methods.


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
    her_dog = Dog('Daisy', 4)
    # call dog methods
    his_dog.get_info()
    his_dog.roll_over()
    his_dog.sit()
    her_dog.get_info()
    her_dog.chase_ball()
