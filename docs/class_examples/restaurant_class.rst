====================================================
Restaurant Class
====================================================
    
| Set the Restaurant's name, food type, open hours on calling the Restaurant classas well as setting the number of tables booked to 0.
| Write a method, get_info(), to print a descriptive line, using f strings: 
| Write methods ot set the number of tables booked and increment them.

.. admonition:: Tasks

    #. Write a Restaurant class scaffolded below.

        .. code-block:: python

            class Restaurant:

                def __init__(self, restaurant_name, food_type, open_hours):
                    self.
                    self.
                    self.
                    self.tables_booked
                    
                def get_info(self):
                    print(f"{                } serves {             } food {             }. {             } tables booked.")

                def set_number_tables_booked(self, tables_booked):
                    '''Set the number of tables booked'''
                    self.
                
                def increment_number_tables_booked(self, new_bookings):
                    ''' Increment the number of customers who've been served'''
                    self.tables_booked
                    
            # instantiate 2 Restaurants
            res_1 = Restaurant("Pierre's", "French", "6-10pm")
            res_2 = Restaurant("Louie's Bistro", "Italian", "10am - 2pm")
            # set booked tables
            res_1.set_number_tables_booked(8)
            res_2.set_number_tables_booked(4)
            res_2.increment_number_tables_booked(2)
            # print info
            res_1.get_info()
            res_2.get_info()

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
                            ''' Increment the number of customers who've been served'''
                            self.tables_booked += new_bookings
                            
                    # instantiate 2 Restaurants
                    res_1 = Restaurant("Pierre's", "French", "6-10pm")
                    res_2 = Restaurant("Louie's Bistro", "Italian", "10am - 2pm")
                    # set booked tables
                    res_1.set_number_tables_booked(8)
                    res_2.set_number_tables_booked(4)
                    res_2.increment_number_tables_booked(2)
                    # print info
                    res_1.get_info()
                    res_2.get_info()
