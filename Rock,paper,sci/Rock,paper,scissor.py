import random
def comp():
    num=random.randint(0,2)
    if num==0:
        computer="r"
    elif num==1:
        computer="s"
    else:
        computer="p"
    return computer    

def game(comp_move):
    tie=True
    while  tie:
        user=input("Enter your move:")
        if comp_move==user:
            tie=True
            print("It is a draw")
        elif (user=="r" and comp_move=="s") or (user=="s" and comp_move=="p") or (user=="p" and comp_move=="r"):
            tie=False
            print("You won!")
        elif (user=="r" and comp_move=="p") or (user=="s" and comp_move=="r") or (user=="p" and comp_move=="s"):
            tie=False
            print("The computer won,You lost!")

def restart():
    re=input("Do you wnat to play again (y/n):")
    if re=="y":
        comp_move=comp()
        game(comp_move)               
        if comp_move=="r":
           print("The computer chose rock")
        elif comp_move=="p":
           print("The computer chose paper") 
        elif comp_move=="s":
           print("The computer chose scissors")
        restart()     
    else:
        print("End game!")

comp_move=comp()
game(comp_move)
if comp_move=="r":
    print("The computer chose rock")
elif comp_move=="p":
    print("The computer chose paper") 
elif comp_move=="s":
    print("The computer chose scissors") 
restart()         