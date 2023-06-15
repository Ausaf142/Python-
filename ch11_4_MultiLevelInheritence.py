#GYAN KI BAAT---Inheritence pe property ek ki dusre k pas ajati hai hai
#rahi baat ambiguity k to ni hota hai same name hai to jo pahle likha gya hai jo child k parameter mein (inheritate hua by name) jo pahle likha hai usk execute hoga
#rahi bat same name mtd multiLevel mein to jo parents sabse najdik hoga us class k method execute hoga
#sabse pahle khud me dekhega wha ni to just upar wale parents ,eim dekhega hai us k bad ni to us k upr wala wrna usk upr wala 
#kai ni hai to error dega


class Person:
    country="India"

    def takeBreak(self):
         print("i am breathing")


class Employee(Person):
    salary=10000
    company="honda"
    def getsalary(self):
        print(f"Salary is {self.salary}")

    def takeBreak(self):
         print("I am an Employee so i am breathing also")            

class Programmer(Employee):
    company="fiverr"
    def getsalary(self):
        print(f"No salary to programmers")

    def takeBreak(self):
        super().takeBreak()
        print("I am an Employee so i am luckily  breathing also")      

# p=Person()
# # print(p.country)
# p.takeBreak()


# e=Employee()
# # print(e.company)   
# # print(e.country)
# e.takeBreak()


pr=Programmer()
# print(pr.company)
# print(pr.country)
# pr.getsalary()
# pr.getsalary()
pr.takeBreak()