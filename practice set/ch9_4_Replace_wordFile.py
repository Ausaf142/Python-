with open("sample.txt") as f:
    content=f.read()
c=content.replace("donkey","$%$%$%$")

with open("sample.txt","w") as f:
   f.write(c)