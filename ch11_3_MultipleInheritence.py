class Employee:
    company="Visa"
    eCode=120

class Freelancer:
    company="Fiverr"    
    level=0
    def upgradeLevel(self):
        self.level=self.level+1

class Programmer(Employee,Freelancer):
    name="Rohit"

p=Programmer()
p.upgradeLevel() #here upgradLvel has change the value now level is 1 from 0/after that calling level will give us result 1 instead 0 
print(p.level)
print(p.company)   #Ambiguity is form--bt it is solved in python/it depends on the priority in seq given in the parameter of child object
 #like we have "class Programmer(Employee,Freelancer)"--which at first that method will execute at the time of ambiguity