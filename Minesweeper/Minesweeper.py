import random

def print_board(game_board):
    count=0
    for i in game_board:
        for j in i:
            print(str(j)+"|",end="")
            count+=1
            if j==9:
                print("\n_____________")
            if count==10:
                print("\n")
                count=0 

def create_grid(bomb):
    count=0
    #Assign bombs
    bomb_list=[""]
    board_1=[[" ",1,2,3,4,5,6,7,8,9],
       [1," "," "," "," "," "," "," "," "," "],
       [2," "," "," "," "," "," "," "," "," "],
       [3," "," "," "," "," "," "," "," "," "],
       [4," "," "," "," "," "," "," "," "," "],
       [5," "," "," "," "," "," "," "," "," "],
       [6," "," "," "," "," "," "," "," "," "],
       [7," "," "," "," "," "," "," "," "," "],
       [8," "," "," "," "," "," "," "," "," "],
       [9," "," "," "," "," "," "," "," "," "]]
    for i in range(1,11):
        row=random.randint(1,9)
        col=random.randint(1,9)
        if (row,col) in bomb_list:
            i-1
            continue
        bomb_list.append((row,col)) 
        board_1[row][col]=bomb
    #Assign zeros or numbers
    for i in range(len(board_1)):
        for j in range(len(board_1[0])):
            r=i
            c=j
            if board_1[r][c]==" ":        
                for z in range(r-1,r+2):
                    if z>0 and z<=9 and z!=r:
                       if board_1[z][c]==bomb:
                          count=count+1
                for z in range(c-1,c+2):
                    if z>0 and z<=9 and z!=c:
                       if board_1[r][z]==bomb:
                          count=count+1
                for z in range(c-1,c+2):
                    if z>0 and z<=9 and r+1<=9 and z!=c:
                       if board_1[r+1][z]==bomb: 
                          count=count+1
                for z in range(c-1,c+2):
                    if z>0 and z<=9 and z!=c:
                       if board_1[r-1][z]==bomb: 
                          count=count+1
                board_1[r][c]=count
                count=0                                                                
    return board_1,bomb_list

def open_neighbour(game_board,i,j,full_board):
    col=[]
    for x in range(i,0,-1):
        if x>0:
           for y in range(j,0,-1):
               if y>0:
                    if y in col:
                       break
                    elif full_board[x][y]!="*":
                     game_board[x][y]=full_board[x][y]
                    elif full_board[x][y]=="*":
                      col.append(y)
                      break
    col=[]                                  
    for x in range(i,0,-1):
        if x>0:
           for y in range(j,10):
               if y<=9:
                    if y in col:
                       break
                    elif full_board[x][y]!="*":
                     game_board[x][y]=full_board[x][y]
                    elif full_board[x][y]=="*":
                        col.append(y)
                        break
    col=[]                
    for x in range(i,10):
        if x<=9:
           for y in range(j,0,-1):
               if y>0:
                    if y in col:
                       break
                    elif full_board[x][y]!="*":
                      game_board[x][y]=full_board[x][y] 
                    elif full_board[x][y]=="*" :
                        col.append(y)
                        break
    col=[]                
    for x in range(i,10):
        if x<=9:
           for y in range(j,10):
               if y<=9:
                    if y in col:
                       break
                    elif full_board[x][y]!='*':
                     game_board[x][y]=full_board[x][y]  
                    elif full_board[x][y]=="*":
                        col.append(y)
                        break 
    return game_board

def check_empty(game_board):
    for i in game_board:
        for j in i:
            if j==" ":
                return True
    return False 

game_board=[[" ","1","2","3","4","5","6","7","8","9"],
       ["1"," "," "," "," "," "," "," "," "," "],
       ["2"," "," "," "," "," "," "," "," "," "],
       ["3"," "," "," "," "," "," "," "," "," "],
       ["4"," "," "," "," "," "," "," "," "," "],
       ["5"," "," "," "," "," "," "," "," "," "],
       ["6"," "," "," "," "," "," "," "," "," "],
       ["7"," "," "," "," "," "," "," "," "," "],
       ["8"," "," "," "," "," "," "," "," "," "],
       ["9"," "," "," "," "," "," "," "," "," "]]
bomb="*"
full_board,boom=create_grid(bomb)
lost=False
won=False
Moves=0
print_board(game_board)
while not lost and not won :
      # user input
    row,col=input("Enter where you want to dig (row,col):").split(",")
    if full_board[int(row)][int(col)]==bomb:
        print("You hit a mine, you lose!")
        game_board[int(row)][int(col)]=bomb
        lost=True
    elif full_board[int(row)][int(col)]==0:
        game_board[int(row)][int(col)]=0
        game_board=open_neighbour(game_board,int(row),int(col),full_board)    
    else:
        game_board[int(row)][int(col)]=full_board[int(row)][int(col)]
    if not check_empty(game_board):
        print("You won!")
        game_board=full_board
        won=True
    print_board(game_board)     

