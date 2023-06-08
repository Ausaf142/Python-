#use open function to read file
#f=open("sample.txt","r")
#'r' is remain bydefault we can go for without writting "r"

f=open("sample.txt","r")
data=f.read()
# data=f.read(5)  #one time read use hoga /jitna tak padhna hai hum numbers de skte hai
print(data)
f.close()