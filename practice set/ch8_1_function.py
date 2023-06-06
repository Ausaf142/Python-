def greatest(n1,n2,n3):
    if(n1>n2):
        if(n1>n3):
            return n1
        else:
           return n3
    else:
        if(n2>n3):
            return n2
        else:
            return n3

max=greatest(12,100,79)    
print(f"greatest is{max}")           #ways of printing 3-ways    
print("greates is " +str(max))
print("greates is " ,max)
