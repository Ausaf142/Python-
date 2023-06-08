with open("Poem.txt",) as f:  #by default read"r" is present already
    a=f.read()
if "Twinkle" in a:
    print("Yes twinkle is present")

else:
    print("Not present")
f.close()
