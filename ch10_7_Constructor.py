class Employee:
     Company="google"
     salary=100000
     def __init__(self,name,salary,subunit):   #Constructor ek bar initiate krdo fir cal krlo jitne function ,td hai usme
          print("Employee is created")
          self.name=name
          self.salary=salary
          self.subunit=subunit
         
     def getDetails(self):
          print(f"The name of the employee {self.name}")
          print(f"The salary of the employee {self.salary}")
          print(f"The unit of the employee {self.subunit}")

     def getSal(self,signature):
         
          print(f"Salary for this employee working is {self.salary} in {self.Company}\n{signature}")
         

     @staticmethod          
     def greet():               
          print("Good Morning")   

Adeeb = Employee("sufi",200000,"jadu")
# Adeeb.salary="50lakh"
Adeeb.getDetails()

           