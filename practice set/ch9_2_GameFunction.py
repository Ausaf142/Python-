def game():

    return 100

#as we knw file mein string sava hota hai,to usi hisab se str()use krenege humlog

score=game()   
with open("HiScore.txt") as f:
    hiscore=(f.read())
if hiscore=="":
      with open("HiScore.txt","w") as f:
        f.write(str(score))
if int(hiscore)<score:
    with open("HiScore.txt","w") as f:
        f.write(str(score))

