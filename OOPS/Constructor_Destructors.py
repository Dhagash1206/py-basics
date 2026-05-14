class Employee:
    def __init__(self, name, salary):       # Constructor
        self.name = name
        self.__salary = salary
        print(f"Employee {self.name} created")

    def get_salary(self):
        return self.__salary

    def show_details(self):
        print(f"Name: {self.name}, Salary: {self.get_salary()}")

    def __del__(self):                      # Destructor
        print(f"Employee {self.name} removed from memory")


# Usage
emp1 = Employee("ABC", 80000)   # Constructor called 
emp1.show_details()              


del emp1  # Destructor called 

# __init__ and __del__ are predefined 