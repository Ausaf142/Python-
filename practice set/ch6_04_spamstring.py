text = input("Enter the text")
spam=False
if("make a lot of money" in text):
    spam=True
elif("buy now" in text):
    spam=True
elif("click this" in text):
    spam=True
elif("suscribe this" in text):
    spam=True
else:
    spam=False

if(spam):
    print("This is spam")
else:
    print("This is not spam")