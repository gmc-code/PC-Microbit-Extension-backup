====================================================
User Class
====================================================
    
| Set the user first_name, last_name, date_of_birth
| Call the user methods.


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