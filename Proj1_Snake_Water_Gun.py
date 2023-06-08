import random
def game(comp,you):
    if comp==you:
        return None
    elif comp=="s":
        if you=="w":
            return False
        elif you=="g":
            return True
    elif comp=="w":
        if you=="g":
            return False
        elif you=="s":
            return True
    elif comp=="g":
        if you=="s":
            return False
        elif you=="w":
            return True
        

              
print("Computer turn:Snake(s) water(w) or Gun(g)")
randomNum=random.randint(1,3)
if randomNum==1:
    comp="s"
elif randomNum==2:
    comp="w"
elif randomNum==3:
    comp="g"


you=input("your's turn:Snake(s) water(w) or Gun(g)?:\n")

a=game(comp,you)

if a==None:
    print("The game is tie")
elif a==True:
    print("Hurrah!You Win")    
else:
    print("You Loose")    
print(f"Computer choosed:{comp}")
print(f"You choosed:{you}")    