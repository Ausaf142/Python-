class Employee:
    company="Camel"
    salary=100
    location="delhi"
    # def changeSalary(self,sal):  #instance attributre of class is changed but main value will remain same wht is written
    #     self.salary=sal              #tunder mtd

#----------->Ye class k actual value ko change krta hai
    @classmethod
    def changeSal(cls,sal):
        cls.salary =sal        
e=Employee()
print(e.salary)    
e.changeSal(455)
print(e.salary) 
print(Employee.salary)