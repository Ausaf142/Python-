content=True
i=1
with open("log.txt") as f:
    while content:
        content=f.readline()
        if 'python' in content.lower():
                print(content)
                print("YES,python is in log text line number: "+str(i)) 
        i=i+1
    
        

