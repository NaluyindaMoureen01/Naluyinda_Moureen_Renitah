class Employee:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Employee Name: {self.name}")

class Manager(Employee):
    def display_info(self):
        print(f"Manager: {self.name}")

class Developer(Employee):
    def display_info(self):
        print(f"Developer: {self.name}")

employee = Employee("Alex")
manager = Manager("Linda")
developer = Developer("John")

employee.display_info()  
manager.display_info() 
developer.display_info() 
