# Parent Class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def show_details(self):
        print(f"Name: {self.name}, Salary: {self.get_salary()}")

    def work(self):
        print(f"{self.name} is working")


# Child Class 1
class Manager(Employee):
    def manage_team(self):
        print(f"{self.name} is managing the team")


# Child Class 2
class Developer(Employee):
    def write_code(self):
        print(f"{self.name} is writing code")


# Usage
mgr = Manager("ABC", 80000)
mgr.show_details()
mgr.work()              
mgr.manage_team()

dev = Developer("xyz", 60000)    
dev.show_details()      
dev.write_code()        