import random
def user(num):
    guessno=3
    while guessno!=0:
        guess=int(input("Enter your guess from (0 to 20):"))
        if(guess>num):
            print("Guess is to high")
        elif(guess<num):
            print("Guess is to low")
        elif guess==num:
           print("You have guessed correctly,you win!")
           break
        guessno=guessno-1 
        print(f"You have {guessno} guesses left")
    if guessno==0:      
       print("You are out of guesses,you lose!")                
          
num=random.randint(0,20)
user(num)
