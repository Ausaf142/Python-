mydict ={
        "pankha":"Fan",
        "Dabba":"Bucket",
        "vastu":"item"

}
print("Your options:",mydict.keys())
a=input("Enter the Hindi Word\n")
# print("The English Word of Your" ,a,"is:",mydict[a])       # we should avoid to occur error so when input is 
                                                             # not present then it give error

print("The English Word of Your" ,a,"is:",mydict.get(a))     # So we will give use get() for return like NONE
