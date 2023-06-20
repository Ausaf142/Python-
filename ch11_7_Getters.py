class Employee:
    company="Bharat Gas"
    salary=5600
    salarybonus=500
    # totalSalary=6100

    @property    #hai function but ye as property kam karega matlb call hum jo krenge wo ayega output yha se add multiply ho kr
    def totalSalary(self):
        return self.salary+self.salarybonus
    
    @totalSalary.setter
    def totalSalary(self,val):
        self.salarybonus= val-self.salary
e=Employee()
print(e.totalSalary)
e.totalSalary=5700
print(e.salarybonus)
print(e.salary)
   