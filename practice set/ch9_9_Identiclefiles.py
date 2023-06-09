file1="log.txt"
file2="this.txt"

with open(file1) as f:
   f1= f.read()

with open(file2) as j:
   f2= j.read()

if (f1==f2):
   print("files are identicle")
else:
   print("files are Not identicle")