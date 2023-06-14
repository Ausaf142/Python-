class Employee:
    Company="google"

Ram=Employee() #yaha hum object create kr rhe hai/loi bhu name lo ar usk eql class name with bracket
Shyam=Employee()
print(Ram.Company)
print(Shyam.Company)
Employee.Company="Youtube"  #hum yha direct class name k ref se value change kr rhe hai
print(Ram.Company)
print(Shyam.Company)
