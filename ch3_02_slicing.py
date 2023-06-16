greeting = "good morning, "
name="adeeb"
c= greeting+name
#concatinating two string  whatevr u want
print(c)
print(name[3])
#name[3]="d"   #-->it is not permissable to change the value at any index

#slicing-->#help of index we can get the alphabates (providing range under the length)
print(name[2:5])  #range ek kum rhta hai like 2:4--start hoga 2 index se jayega 3 tak
print(name[:4]) #agar vaccant chorda to by default minumum zero lelega
print(name[0:]) # agar last tk chahye to max length le lega(0-5)
print(name[-5]) #negative mein -1 se start hota hai lst tk,zero se ni hota hai start