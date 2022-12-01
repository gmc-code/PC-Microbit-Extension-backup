====================================================
User Class
====================================================
    
| Set the user first_name, last_name, date_of_birth
| Call the user methods.

| Set the User's first_name, last_name, date_of_birth on calling the User class, as well as setting the number of logins to 0.
| Write the methods, get_info() and get_login_info(self) to print a descriptive line, using f-strings: 
| Write a greeting method, greet_user().
| Write a method to reset the number of logins and a method to increment them.

.. admonition:: Tasks

    #. Write a User class scaffolded below.

        .. code-block:: python

            class User:
                def __init__(self, first_name, last_name, date_of_birth):
                    self.first_name = 
                    self.last_name = 
                    self.date_of_birth = 
                    self.logins = 

                def get_info(self):
                    print(f"{       first_name} {      last_name} was born {      date_of_birth}.")

                def get_login_info(self):
                    print(f"{     first_name} {      last_name} has logged in {     logins} times.")

                def greet_user(self):
                    print(f"Welcome, {      first_name}!")

                def increment_logins(self):
                    self.logins += 1
                    print(f"logins: {               }")

                def reset_logins(self):
                    self.logins = 0
                    print(f"logins: {             }")
                    
                    
            user_1 = User("Tim", "Lum", "1999-12-24")
            user_2 = User("Kim", "Zhang", "2002-03-13")

            user_1.greet_user()
            user_1.get_info()
            user_1.increment_logins()
            user_1.get_login_info()


        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a class for a Restaurant.

                .. code-block:: python

                class User:
                    def __init__(self, first_name, last_name, date_of_birth):
                        self.first_name = first_name
                        self.last_name = last_name
                        self.date_of_birth = date_of_birth
                        self.logins = 0

                    def get_info(self):
                        print(f"{self.first_name} {self.last_name} was born {self.date_of_birth}.")

                    def get_login_info(self):
                        print(f"{self.first_name} {self.last_name} has logged in {self.logins} times.")

                    def greet_user(self):
                        print(f"Welcome, {self.first_name}!")

                    def increment_logins(self):
                        self.logins += 1
                        print(f"logins: {self.logins}")

                    def reset_logins(self):
                        self.logins = 0
                        print(f"logins: {self.logins}")
                        
                        
                user_1 = User("Tim", "Lum", "1999-12-24")
                user_2 = User("Kim", "Zhang", "2002-03-13")

                user_1.greet_user()
                user_1.get_info()
                user_1.increment_logins()
                user_1.get_login_info()