a={}
print(type(a)) #Set nahi hai ye dictionary create hoga 


c={1,2} #agar object hai ander to direct create hoga
print(type(c)) 


#empty set created by follow
b =set()
print(type(b))
b.add(5)
b.add(9)
#Mtalab jo hum baad be bhi edit,update,insert kr skte hai wo set me add n hoga
# b.add({1,2})  #we cant add list into set because it is changable further next but set is not
b.add((2,99)) #tupple can be addede to set bcz we cant change tupple
#b.add({"boy":"ausaf"})  #we cant add Dictionary into set because it is changable further next but set is not
#b[0]=0  #proved set assign or change ni ho skta
print(b)
# set are unordred,unindex,cant assignmed later,no duplicated