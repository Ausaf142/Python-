class Employee:
    salary=1000
    increment=1.5
    @property
    def salaryAfterIncreament(self):
        return self.salary*self.increment
    
    @salaryAfterIncreament.setter
    def salaryAfterIncreament(self,Fsal):
       self.increment=Fsal/self.salary


e = Employee()
print(e.increment)
e.salaryAfterIncreament=2000
print(e.salaryAfterIncreament)       
print(e.increment)