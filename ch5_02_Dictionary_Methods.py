myDict ={
    "fast":"In a Quick Manner",
    "Harry":"A coder",
    "Marks": [1,2,3],
    "anotherdict": {'harry':'player'},
    1:2
}
print(myDict.keys())        #it display the keys
print(type(myDict.keys()))  #it display the type of keys
print(list(myDict.keys()))  #type ko list mein cast kr skte hai
print(list(myDict.values())) #it display the values
print(myDict)
updateDict={                #update or we can add some more
    "loveish":"friend"      #duplicate can also be update it will update

}
myDict.update(updateDict)
print(myDict)
print(list(myDict.keys()))
print(myDict.get("Harry1"))     #if not available it give none in return
print(myDict["Harry1"])         #it give error which will stop the result