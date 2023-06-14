class programmer:
    company="Microsoft"
    def __init__(self,name,product):
        self.name=name
        self.product=product

    def getInfo(self):
        print(f"The name of the programmer is {self.name} and product is {self.product}")

alka=programmer("Alka","skype")
janu=programmer("Janu","Github")
alka.getInfo()
janu.getInfo()