class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary      # private attribute

    # Public method
    def show_name(self):
        print(f"Employee: {self.name}")

    # Private method 
    def __calculate_bonus(self):
        return self.__salary * 0.10

    # Private method 
    def __get_salary(self):         # salary now in private function
        return self.__salary

    # Public method accessing both private methods
    def show_salary_details(self):
        salary = self.__get_salary()
        bonus = self.__calculate_bonus()
        print(f"Salary: {salary}, Bonus: {bonus}")


emp = Employee("abc", 50000)

print(emp.name)               
emp.show_name()               
emp.show_salary_details()     

# Private - will FAIL
# print(emp.__salary)         # Error
# emp.__calculate_bonus()     # Error
# emp.__get_salary()          # Error

