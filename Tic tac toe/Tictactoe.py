import random
from re import A

def pri_board(board):
    count=0
    for rows in board:
        print(" "+rows+" |",end="")
        count+=1
        if count==3:
            count=0
            print("\n")
    return board

def pri_board_1(board_1):
    count=0
    for rows in board_1:
        print(" "+rows+" |",end="")
        count+=1
        if count==3:
            count=0
            print("\n")
    return board_1   

def game(board,let,board_1):
    move=input("Enter your move:").upper()
    if move  not in let:                 
        for rows in board:
            if move==rows:  
                ind=board.index(move)
                board_1[ind]="X"
        let.append(move)              
    else:
        print("Invalid move")    
    while True:                                                                      
        comp=random.choice(board)
        if comp not in let:                                  
            for rows in board:
                for col in rows:
                    if comp==col:
                       ind=board.index(comp)
                       board_1[ind]="O"
            let.append(comp)               
            print(f"The computer moved to:{comp}")
            break
    pri_board_1(board_1)
    return let

def check_win_user(board_1,win):
    if board_1[0]=="X" and board_1[0]==board_1[1]==board_1[2]:
       win=True
       print("Player wins")
    elif board_1[3]=="X" and board_1[3]==board_1[4]==board_1[5]:
        win=True
        print("Player wins")
    elif board_1[6]=="X" and board_1[6]==board_1[7]==board_1[8]:
        win=True
        print("Player wins")
    elif board_1[0]=="X" and board_1[0]==board_1[3]==board_1[6]:
        win=True
        print("Player wins")
    elif board_1[1]=="X" and board_1[1]==board_1[4]==board_1[7]:
        win=True
        print("Player wins") 
    elif board_1[2]=="X" and board_1[2]==board_1[5]==board_1[8]:
        win=True
        print("Player wins")
    elif board_1[0]=="X" and board_1[0]==board_1[4]==board_1[8]:
        win=True
        print("Player wins")
    elif board_1[2]=="X" and board_1[2]==board_1[4]==board_1[6]:
        win=True
        print("Player wins")
    return win   

def check_win_comp(board_1,win):
    if board_1[0]=="O" and board_1[0]==board_1[1]==board_1[2]:
       win=True
       print("Computer wins")
    elif board_1[3]=="O" and board_1[3]==board_1[4]==board_1[5]:
        win=True
        print("Computer wins")
    elif board_1[6]=="O" and board_1[6]==board_1[7]==board_1[8]:
        win=True
        print("Computer wins")
    elif board_1[0]=="O" and board_1[0]==board_1[3]==board_1[6]:
        win=True
        print("Computer wins")
    elif board_1[1]=="O" and board_1[1]==board_1[4]==board_1[7]:
        win=True
        print("Computer wins") 
    elif board_1[2]=="O" and board_1[2]==board_1[5]==board_1[8]:
        win=True
        print("Computer wins")
    elif board_1[0]=="O" and board_1[0]==board_1[4]==board_1[8]:
        win=True
        print("Computer wins")
    elif board_1[2]=="O" and board_1[2]==board_1[4]==board_1[6]:
        win=True
        print("Computer wins")
    return win    


          
board=["A","B","C","D","E","F","G","H","I"]
board_1=[" "," "," "," "," "," "," "," "," "]
let=[" "]
turns=0
win=False
print("Welcome to tic tac toe\nThe player moves with 'X' and the computer with 'O'")
pri_board(board)
while turns<9:
    game(board,let,board_1)
    user_wins=check_win_user(board_1,win)
    comp_wins=check_win_comp(board_1,win)
    if user_wins or comp_wins:
        break 
    turns+=1
if turns==9 and not user_wins and not comp_wins:
    print("It is a draw")        
