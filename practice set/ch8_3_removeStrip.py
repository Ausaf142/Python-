# this="     Ausaf is good boy   "
# print(this)
# print(this.strip())#strip extra space both end hatata hai

def remove_split(string ,word):
    newStr=string.replace(word,"")
    return newStr.strip()



This ="     Adib is Good boy    "
n =remove_split(This,"Adib")
print(n)