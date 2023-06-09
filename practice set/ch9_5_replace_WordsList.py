
words=["donkey","kutta","sala"]


with open("sample.txt") as f:
    content=f.read()

for word in words:    
    content=content.replace(word,"$%$%$%$") #yaha koi b change hume store krna hota hai ar yha usi name se krenge taki 
                                            #one by one sara change ho 
with open("sample.txt","w") as f:
    f.write(content)