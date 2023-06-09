with open("log.txt") as f:
    content=f.read().lower()
if "python" in content:
    print("YES,python is in log") 
else:
    print("No python is not present")
