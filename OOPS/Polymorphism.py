class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def work(self):
        print(f"{self.name} is doing general work")

    def show_details(self):
        print(f"Name: {self.name}, Salary: {self.get_salary()}")


class Manager(Employee):
    def work(self):                     # overrides parent
        print(f"{self.name} is managing team")

    def show_details(self):             # overrides parent
        print(f"[Manager] Name: {self.name}, Salary: {self.get_salary()}")


class Developer(Employee):
    def work(self):                     # overrides parent
        print(f"{self.name} is writing code")

    def show_details(self):             # overrides parent
        print(f"[Developer] Name: {self.name}, Salary: {self.get_salary()}")


class Intern(Employee):
    def work(self):                     # overrides parent
        print(f"{self.name} is learning and assisting")

    def show_details(self):             # overrides parent
        print(f"[Intern] Name: {self.name}, Salary: {self.get_salary()}")


# Usage - Method Overriding
emp1 = Manager("ABC", 80000)
emp2 = Developer("XYZ", 70000)
emp3 = Intern("EMP1", 30000)

emp1.work()             # ABC is managing team
emp2.work()             # XYZ is writing code
emp3.work()             # EMP1 is learning and assisting

emp1.show_details()     # [Manager] Name: ABC, Salary: 80000
emp2.show_details()     # [Developer] Name: XYZ, Salary: 60000
emp3.show_details()     # [Intern] Name: EMP1, Salary: 20000


for emp in [emp1, emp2, emp3]:
    emp.work()          # same call, different behavior
    emp.show_details()


class HR(Employee):
    def calculate_bonus(self, percentage=10, extra=0):  # overloading simulation
        salary = self.get_salary()
        bonus = (salary * percentage / 100) + extra
        print(f"Bonus for {self.name}: {bonus}")
