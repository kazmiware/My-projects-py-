class N_queens:
    board=[]
    cor=[]
    used=[]

    def __init__(self,N_Q,row,col):
        self.queens="Q"
        self.N_Q=N_Q #No of queens
        self.row=row
        self.col=col

    def create_board(self):
        for i in range(self.row):
            lst=[]
            for j in range(self.col):
                lst.append(0)
            self.board.append(lst)

    def solve(self,x,y):
        if self.check_board():
            return True

        if x==0 and self.used!=[]:
            self.used=list(filter(lambda a:a[0]==0,self.used))

        if self.check_box(x,y) and (x,y) not in self.used:
                self.board[x][y]=self.queens
                self.cor.append((x, y))
                if x+1 in range(len(self.board[0])):
                    x_new = x + 1
                else:
                   x_new=x
                y_new=0
                if self.solve(x_new,y_new):
                    return True
        else:
            if y+1 in range(len(self.board[0])):
               y_new=y+1
               self.solve(x,y_new)
            else:
                prev_x,prev_y=self.cor[-1]
                self.cor.remove((prev_x,prev_y))
                self.used.append((prev_x,prev_y))
                self.board[prev_x][prev_y]=0
                if prev_y+1 in range(len(self.board[0])):
                   prev_y=prev_y+1
                   self.solve(prev_x,prev_y)
                else:
                       x_new=prev_x
                       y_new=0
                       self.solve(x_new,y_new)


    def check_box(self,x,y):
        for i in range(len(self.board)):
            if x-i in range(self.row) and y in range(self.col):
               if self.board[x-i][y]==self.queens:
                   return False

        j=0
        while x+j in range(self.row) and y+j in range(self.col):
                   if self.board[x+j][y+j]==self.queens:
                        return False
                   j+=1

        j=0
        while x-j in range(self.row) and y-j in range(self.col):
                   if self.board[x-j][y-j]==self.queens:
                        return False
                   j += 1

        j=0
        while x-j in range(self.row) and y+j in range(self.col):
               if self.board[x-j][y+j]==self.queens:
                    return False
               j += 1

        j=0
        while x+j in range(self.row) and y-j in range(self.col):
               if self.board[x+j][y-j]==self.queens:
                    return False
               j += 1
        return True


    def check_board(self):
        count=0
        for i in self.board:
            for j in i:
                if j==self.queens:
                    count+=1
        if count==self.N_Q:
            return True
        return False

    def print_board(self):
        for i in self.board:
            print(i)



board1=N_queens(4,4,4)
board1.create_board()
board1.solve(0,0)
board1.print_board()