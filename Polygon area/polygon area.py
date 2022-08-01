from cmath import sqrt
import math

import math
class rectangle:
    def __init__(self,height,width):
        self.height=height
        self.width=width

    def set_height():
        rectangle.height=input("Enter height:")    
 
    def set_width():
        rectangle.width=input("Enter width:")    

    def rect_area():
        print("Area="+str(int(rectangle.height)*int(rectangle.width)))
    
    def rect_Perimeter():
        print("Perimeter="+str(2*(int(rectangle.height)+int(rectangle.width))))

    def rect_diagonals():
        sq_width=pow(int(rectangle.width),2) 
        sq_height=pow(int(rectangle.height),2)
        dig="{:.2f}".format(sqrt(sq_height+sq_width).real)
        print("Diagonals="+str(dig))

    def print_shape(h,w):
        for i in range(int(h)):
            for j in range(int(w)):
                print("*",end="")
            print("\n") 

    def fit_shape(sides):
        num_1=int(rectangle.height)/int(sides)
        num_2=int(rectangle.width)/int(sides)
        print(f"The number of squares that can be fitted in this triangles is:{num_1*num_2}")

        


class square(rectangle):
    def __init__(self) -> None:
        super().__init__()
       
    def sq_sides():
        square.height=input("Enter height of sqaure:")
        square.width=square.height
        return square.height,square.width

    def sq_area():
        Area=int(square.height)+int(square.height)
        print("Area="+str(Area))    
        
    def sq_perimeter():
        peri=4*int(square.height)
        print("perimeter="+str(peri)) 

    def sq_diagonal():
        dig="{:2f}".format(sqrt(2).real*int(square.height))
        print("Diagonals="+str(dig))      

choice=None
while choice!=0:
    print("Area calculator:")
    print("1)Area & perimeter of rectangle\n2)Area & perimeter of square\n0)Exit")
    choice=input("Enter your option:")
    if choice==1:
        rectangle.set_height()
        rectangle.set_width
        rectangle.rect_area()
        rectangle.rect_Perimeter()
        rectangle.rect_diagonals()
        rectangle.print_shape()
    elif choice==2:
        square.sq_sides()
        square.sq_area()
        square.sq_perimeter()
        square.sq_diagonal()
        square.print_shape()    