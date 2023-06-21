import random
randomNumber = random.randint(1,100)
print(randomNumber)
userGuess=None
guesses=0
while(userGuess !=randomNumber):
    userGuess=int(input("Enter the Number "))
    if(userGuess==randomNumber):
        print("You guessed it right")
        print(f"number is {randomNumber} and finally u gave {userGuess} number,So You WIN")
       
    else:
        if(userGuess>randomNumber):
         print("You guessed it wrong!  Enter a smaller number")  
        else:
           print("You guessed it wrong!  Enter a Bigger number")  
    guesses +=1

print("Your number of Approuch is:", guesses)

with open("HighScoreRandom.txt","r") as f:
   highScore=int(f.read())
if(guesses<highScore):
 print("Created new High Score")
 with open("HighScoreRandom.txt","w") as f:
   f.write(str(guesses))