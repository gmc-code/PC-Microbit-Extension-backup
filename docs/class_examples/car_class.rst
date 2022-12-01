====================================================
Car Class
====================================================
    
| Set the car's make, model, year, colour. 
| Use the car's methods to update and read the odometer.


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
