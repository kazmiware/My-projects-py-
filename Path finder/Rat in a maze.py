class path_finder:
    maze=[ [ 1, 0, 0, 0, 0 ],
           [ 1, 1, 1, 1, 1 ],
           [ 1, 1, 1, 0, 1 ],
           [ 0, 0, 0, 0, 1 ],
           [ 0, 0, 0, 0, 3 ]]

    sol_grid=[ [ 0, 0, 0, 0, 0 ],
               [ 0, 0, 0, 0, 0 ],
               [ 0, 0, 0, 0, 0 ],
               [ 0, 0, 0, 0, 0 ],
               [ 0, 0, 0, 0, 0 ]]
    cor=[]

    def __init__(self,end,wall):
        self.end=end
        self.wall=wall

    def solve(self,x,y):
        if self.reach_end(x,y):
            self.sol_grid[x][y]=1
            self.print_sol()
            return True

        if self.move(x,y):
            self.sol_grid[x][y]=1
            self.cor.append((x,y))
            y_new=y+1
            if self.solve(x,y_new):
                return True
            self.cor.remove((x,y))

        if self.move(x,y):
                self.sol_grid[x][y]=1
                self.cor.append((x,y))
                x_new=x+1
                if self.solve(x_new,y):
                    return True
                self.cor.remove((x,y))

        if self.move(x,y):
                self.sol_grid[x][y]=1
                self.cor.append((x,y))
                y_new=y-1
                if self.solve(x,y_new):
                    return True
                self.cor.remove((x,y))

        if self.move(x,y):
                self.sol_grid[x][y]=1
                self.cor.append((x,y))
                x_new=x-1
                if self.solve(x_new,y):
                    return True
                self.cor.remove((x,y))

    def reach_end(self,x,y):
        if y in range(len(self.maze[0])) and x in range(len(self.maze)):
           if self.maze[x][y]==self.end:
               return True

    def move(self,x,y):
        if y in range(len(self.maze[0])) and x in range(len(self.maze)):
           if self.maze[x][y]==1 and (x,y) not in self.cor:
               return True

    def print_sol(self):
        for i in self.sol_grid:
            print(i)


rat=path_finder(3,0)
rat.solve(0,0)




