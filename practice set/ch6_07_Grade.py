# marks = int(input("Enter your marks"))
# if(marks>=90 and marks<=100):
#     print("Grade : EX")
# elif(marks>=80 and marks<=90):
#     print("Grade : A")
# elif(marks>=70 and marks<=80):
#     print("Grade : B")
# elif(marks>=60 and marks<=70):
#     print("Grade : C")
# elif(marks>=50 and marks<=60):
#     print("Grade : D")
# elif(marks<50):
#     print("Grade : F")

marks = int(input("Enter your marks\n"))
grade=False

if(marks>100 ):
      grade="Wrong input"
elif(marks>=90 ):
         grade="Ex"
elif(marks>=80):
   grade="A"
elif(marks>=70):
       grade="B"
elif(marks>=60):
       grade="C"
elif(marks>=50 ):
       grade="D"
elif(marks<50):
      grade="Fail"
print("Your grade is : "+grade)
