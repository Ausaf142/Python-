l1=[1,8,7,2,21,15]
#li_sorted=l1.sort() #list ko store krne k faida n qk ye direct original item ko change krta hai
#isliye command use kro
l1
print(l1[0:])  #index se b print ho skta hai
l1.sort()
print(l1 ,"sorted")      #sorts the list
l1.reverse() 
print(l1,"reversed")     #reverse krta hai
l1.append(45) 
print(l1,"45 appended")    #add krdeta externally item at the end index
# l1.insert(0,544)  #insert(0,544)-->0 index value hai
l1.insert(7,544)
print(l1,"544 inserted at index 7")  
# l1.pop(2)
l1.remove(21) #remove from list
print(l1,"removed 21")