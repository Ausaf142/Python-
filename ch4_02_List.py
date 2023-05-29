l1=[1,8,7,2,21,15]
#li_sorted=l1.sort() #list ko store krne k faida n qk ye direct original item ko change krta hai
#isliye command use kro
# l1.sort()        #sorts the list
# l1.reverse()    #reverse krta hai
l1.append(45)   #add krdeta externally item at the end index
l1.append(95)
print(l1)
# l1.insert(0,544)  #insert(0,544)-->0 index value hai
l1.insert(7,544)
# l1.pop(2)
l1.remove(21) #remove from list
print(l1)