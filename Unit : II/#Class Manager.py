#Class Manager
#Create a Python program to show how the Manager class inherits attributes and methods from both Person and Employee, and how we can add additional behaviours and properties in the Manager class. Person class contains common attributes like name and age. 

class Person:
    def __init__(self,Name,Age):
        self.Name=Name
        self.Age=Age

    def Display(self):
        print(f"Person info (Name, Age): {self.Name} , {self.Age}")
    
class Employee:
    def __init__(self,EmpId,Salary):
        self.EmpId=EmpId
        self.Salary=Salary

    def Display(self):
        print(f"Employee details ( EmpId, Salary ) : {self.EmpId} , {self.Salary}")
    
class Manager(Person,Employee):
    def __init__(self,Name,Age,EmpId,Salary,Department):
        Person.__init__(self,Name,Age)
        Employee.__init__(self,EmpId,Salary)

        #Manager-Specific attribute
        self.Department=Department
    
    def Display(self):
        Person.Display(self)
        Employee.Display(self)
        print("Department:",self.Department)
    
Man1=Manager("Sanjana",18,"Emp1093",300000,"IT")
Man1.Display()
