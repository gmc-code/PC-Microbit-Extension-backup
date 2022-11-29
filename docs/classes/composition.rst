====================================================
Composition
====================================================

| The examples given are for use in python3 mode in Mu editor and are not microbit specific.
| See: https://www.geeksforgeeks.org/inheritance-and-composition-in-python/
| See: https://medium.com/swlh/the-best-way-to-understand-composition-in-python-5-case-studies-and-solution-4b23a6a2cc38

----

Composition
-----------------

| Composition models a has-a-relationship.
| Use composition to create components that can be reused by multiple classes.

----

Employee Salary
-----------------

.. code-block:: python
        
    class Salary:
        def __init__(self, monthly_income, bonus_rate):
            self.monthly_income = monthly_income
            self.bonus_rate = bonus_rate

        def get_annual_salary(self):
            return (self.monthly_income*12)

        def get_bonus(self):
            return (self.monthly_income * self.bonus_rate / 100)


    class Employee:
        def __init__(self, monthly_income, bonus_rate):
            self.monthly_income = monthly_income
            self.bonus_rate = bonus_rate
            self.cls_salary = Salary(self.monthly_income, bonus_rate)

        def annual_salary(self):
            return "Annual Salary= $" + str(self.cls_salary.get_annual_salary() + self.cls_salary.get_bonus())


    emp = Employee(monthly_income=8000, bonus_rate=5)
    print(emp.annual_salary())

