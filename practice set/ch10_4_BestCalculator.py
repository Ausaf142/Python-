class Calculator:
    def __init__(self,num):
        self.number=num
    def square(self):
       print(f"The square of {self.number} is {self.number**2}")
    def squareRoot(self):
       print(f"The Root of {self.number} is {self.number**0.5}")
    def cube(self):
      print(f"The Cube of {self.number} is {self.number**3}")

    @staticmethod  
    def greet():
       print("**********Welcome to the world best calculator*********")
n=int(input("Enter the Number\n"))       
a= Calculator(n)
a.greet()
a.square()
a.squareRoot()
a.cube()
