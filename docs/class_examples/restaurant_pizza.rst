====================================================
Pizza Restaurant Class
====================================================
    
| Write a PizzaShop class as a child class of the Restaurant class.
| Set the PizzaShop's name, food type, open hours on calling the PizzaShop class, as well as setting the manu.
| Write a method, show_menu(), to print the PizzaShop's menu.

.. admonition:: Tasks

    #. Write a Pizza class as a child class of the Restaurant class, scaffolded below.

        .. code-block:: python

            class Restaurant:

                def __init__(self, restaurant_name, food_type, open_hours):
                    self.restaurant_name = restaurant_name
                    self.food_type = food_type
                    self.open_hours = open_hours
                    self.tables_booked = 0

                def get_info(self):
                    print(f"{self.restaurant_name} serves {self.food_type} food {self.open_hours}. {self.tables_booked} tables booked.")

                def set_number_tables_booked(self, tables_booked):
                    '''Set the number of tables booked'''
                    self.tables_booked = tables_booked

                def increment_number_tables_booked(self, new_bookings):
                    '''Increment the number of tables booked'''
                    self.tables_booked += new_bookings


            class PizzaShop(Restaurant):
                '''child class of Restaurant'''
                
                def __init__(self, restaurant_name, food_type, open_hours):
                             .__init__(restaurant_name, food_type, open_hours)
                    self.menu = ["Capricossa",
                                    "Hawaiian",
                                    "BBQ Chicken",
                                    "Pepperoni",
                                    "Margarita"]
                
                def show_menu(self):
                    print(f"\n{                   } has the following menu:")
                    for menu_item in sorted(self.menu):
                        print(f"\t- {         }")

            # instantiate Restaurant
            res_1 = PizzaShop("Joe's Pizza", "Pizza", "6-10pm")
            res_1.get_info()
            res_1.show_menu()


    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a class for a Restaurant.

                .. code-block:: python

                    class Restaurant:

                        def __init__(self, restaurant_name, food_type, open_hours):
                            self.restaurant_name = restaurant_name
                            self.food_type = food_type
                            self.open_hours = open_hours
                            self.tables_booked = 0

                        def get_info(self):
                            print(f"{self.restaurant_name} serves {self.food_type} food {self.open_hours}. {self.tables_booked} tables booked.")

                        def set_number_tables_booked(self, tables_booked):
                            '''Set the number of tables booked'''
                            self.tables_booked = tables_booked
        
                        def increment_number_tables_booked(self, new_bookings):
                            '''Increment the number of tables booked'''
                            self.tables_booked += new_bookings


                    class PizzaShop(Restaurant):
                        '''child class of Restaurant'''
                        
                        def __init__(self, restaurant_name, food_type, open_hours):
                            super().__init__(restaurant_name, food_type, open_hours)

                            self.menu = ["Capricossa",
                                            "Hawaiian",
                                            "BBQ Chicken",
                                            "Pepperoni",
                                            "Margarita"]
                        
                        def show_menu(self):
                            print(f"\n{self.restaurant_name} has the following menu:")
                            for menu_item in sorted(self.menu):
                                print(f"\t- {menu_item}")

                    # instantiate Restaurant
                    res_1 = PizzaShop("Joe's Pizza", "Pizza", "6-10pm")
                    res_1.get_info()
                    res_1.show_menu()