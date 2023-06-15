class Employee:
    company="Google"
    def getdetails(self):
        print("This is Employee")
    def getAdd(self):
        print("This is Employee Add")
class Programmer(Employee):  #child class inherited base class
    company="YouTube"
    def getAdd(self):
        print("This is programmer")
    def getdetails(self):
        print("This is programmer  Details")
a=Employee()
b=Programmer()
print(a.company)       
a.getdetails()       
print(a.company)       
b.getAdd() 
#Now Cross Call in different obj ref
a.getAdd()
b.getdetails()
