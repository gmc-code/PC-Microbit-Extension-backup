====================================================
Car Class
====================================================
    
| Use the car's methods to update and read the odometer.

| Set the car's make, model, year, colour on calling the Car class, as well as setting the odometer to 0.
| Write the methods, get_info() and read_odometer(self) to print a descriptive line, using f-strings: 
| Write a greeting method, greet_user().
| Write a method to update the odometer to a spcified amount and a method to increment the odometer by a spcified amount.


.. admonition:: Tasks

    #. Write a Car class scaffolded below.

        .. code-block:: python

            class Car:

                def __init__(self, make, model, year, colour):
                    self.      = make
                    self.      = model
                    self.       = year
                    self.       = colour
                    self.odometer =
                    
                def get_info(self):
                    return f"{       year} {      colour} {      make} {           model}"

                def read_odometer(self):
                    print(f"{self.get_info()} has done {             } km.")

                def update_odometer(self, km):
                    """
                    Set the odometer reading to the given value if greater than current reading
                    """
                    if km >= self.odometer:
                        self. 
                    else: 
                        print("You can't lower km on an odometer!")

                def increment_odometer(self, km):
                    """
                    increase the odometer reading
                    """
                    if km >= 0:
                        self. 
                    else:
                        print("You can't lower km on an odometer!")
                    
                
            my_car = Car('ford', 'territory', 2005, "tan")
            print(my_car.get_info())

            # update odometer using attribute
            my_car.odometer_reading = 20
            my_car.read_odometer()

            # update odometer using method
            my_car.update_odometer(100_000)
            my_car.read_odometer()

            # update odometer using method
            my_car.increment_odometer(275)
            my_car.read_odometer()


    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a class for a Car.

                .. code-block:: python

                    class Car:

                        def __init__(self, make, model, year, colour):
                            self.make = make
                            self.model = model
                            self.year = year
                            self.colour = colour
                            self.odometer = 0
                            
                        def get_info(self):
                            return f"{self.year} {self.colour} {self.make} {self.model}"

                        def read_odometer(self):
                            print(f"{self.get_info()} has done {self.odometer} km.")

                        def update_odometer(self, km):
                            """
                            Set the odometer reading to the given value if greater than current reading
                            """
                            if km >= self.odometer:
                                self.odometer = km
                            else:
                                print("You can't lower km on an odometer!")

                        def increment_odometer(self, km):
                            """
                            increase the odometer reading
                            """
                            if km >= 0:
                                self.odometer += km
                            else:
                                print("You can't lower km on an odometer!")
                            
                        
                    my_car = Car('ford', 'territory', 2005, "tan")
                    print(my_car.get_info())

                    # update odometer using attribute
                    my_car.odometer_reading = 20
                    my_car.read_odometer()

                    # update odometer using method
                    my_car.update_odometer(100_000)
                    my_car.read_odometer()

                    # update odometer using method
                    my_car.increment_odometer(275)
                    my_car.read_odometer()

