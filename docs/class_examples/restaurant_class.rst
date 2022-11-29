====================================================
Restaurant Class
====================================================
    
| Set the Restaurant's rname, food type, open hours.
| Call the Restaurant methods.


.. code-block:: python

    class Restaurant:

        def __init__(self, restaurant_name, food_type, open_hours):
            self.restaurant_name = restaurant_name
            self.food_type = food_type
            self.open_hours = open_hours
            
        def get_info(self):
            print(f"{self.restaurant_name} serves {self.food_type} food {self.open_hours}.")

    # instantiate 2 Restaurants
    res_1 = Restaurant("Pierre's", "French", "6-10pm")
    res_2 = Restaurant("Louie's Bistro", "Italian", "10am - 2pm")
    # call Restaurant method
    res_1.get_info()
    res_2.get_info()