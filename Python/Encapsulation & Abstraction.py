class Employee:
    def __init__(self, name, salary):
        self.__name = name          # Encapsulated attribute
        self.__salary = salary      # Encapsulated attribute

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for salary
    def get_salary(self):
        return self.__salary

    # Setter for salary
    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative.")

# Abstraction: Using the class without knowing internal details
emp = Employee("Alice", 60000)
print(emp.get_name())
print(emp.get_salary())

emp.set_salary(80000)
print(emp.get_salary())

emp.set_salary(-1000)  # Will print error message