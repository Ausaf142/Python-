class Employee:
    Company="google"
    salary=100

Ram=Employee() 
Shyam=Employee()
 #abiguity wala scene hai SO pahle ye check krega object k ander hai to wo print krega 
 # agr ni tb class mein dekhega ar use execute karega


# Ram.salary=300                #instance attribute salary direct to object
# Shyam.salary=500 
print(Ram.Company)
print(Shyam.Company)
print(Ram.salary)
print(Shyam.salary)
#print(Shyam.address)    #it will give error bcz there is no address attribute in class and object
