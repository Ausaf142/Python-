class Employee:
     Company="google"
     salary=100000
     def getSal(self, signature):
         
         print(f"Salary for this employee working is {self.salary} in {self.Company}\n{signature}")


     @staticmethod            #-->isk matlab --Employee.greet()-self fir ni chahye qk self k use bhi n hai isk ander srf msg print ho rha hai
     def greet():               #jaise getSal mein self k ref pe call ho rha attributes but isme ni hai
          print("Good Morning")   

Adeeb = Employee()
#Adeeb.salary="5cr" 
Adeeb.getSal("Thanks")
Adeeb.greet()                   #-->Employee.greet(Adeeb)--actual mein aise hota hai object creation tym pe/hume self param dena hoga