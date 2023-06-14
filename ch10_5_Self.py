class Employee:
     Company="google"
     salary=100000
     def getSal(self):
         
         print(f"Salary for this employee working is {self.salary} in {self.Company}")#-->self.salary matlab "self" parameter k jagah jo bhi obj ref hai us obj ka salary display hoga
    
Adeeb = Employee()  #-->iska matlab hai====="Employee.getSal(Adeeb)"--Auto parameter hota hai isliye self likhte hai
Adeeb.salary="5cr" 
Adeeb.Company="Facebook" #-->but convenient way hai aise "Adeeb=Employee()"--Ab adeeb obj ref hai ==call karo jise bhi
Adeeb.getSal()           #-->obj k attributes to obj priority first wrna class attributes
