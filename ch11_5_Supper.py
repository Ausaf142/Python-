#same hai constructor k sath bhi maslah,wahi super word immediate parent k liye hai
#constructor ho ya 



class Person:
    country="India"
    def __init__(self):
        print("Initializing Person\n")

    def takeBreak(self):  #(Step3)=finally ye print honge us bad seq follow hoga
        print("i am breathing")


class Employee(Person):
    salary=10000
    company="honda"
    def __init__(self):
         super().__init__()
         print("Initializing Employee\n")

    def getsalary(self):
        print(f"Salary is {self.salary}")

    def takeBreak(self):
         super().takeBreak()  #(Step2)=niche wala jb yha bheja to yaha dekha k y bhi kah rha immediate parent k to ar upar jayega
         print("I am an Employee so i am breathing also")            

class Programmer(Employee):
    company="fiverr"
    def __init__(self):
         super().__init__()
         print("Initializing Programmer\n")

    def getsalary(self):
        print(f"No salary to programmers")

    def takeBreak(self):
        super().takeBreak()  #(Step1)=yaha just immediate parent k takebreak ko call karega usk bad apna line execute karega
        print("I am an Employee so i am luckily  breathing")      



pr=Programmer() 
 #teeno class k mtd print ho jayenge consecutively