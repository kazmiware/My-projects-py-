import random
class flips:
    # list of all faces
    faces=[]
    pos=[] # list of all possibilities
    def __init__(self,quantity:int,face_1,face_2):
        self.quantity=quantity
        self.face_1=face_1
        self.face_2=face_2

    # to append all faces to list
    def create_list(self):
        for i in range(self.quantity):
            self.faces.append(self.face_1)
            self.faces.append(self.face_2)
        print("Faces:",end="")
        for i in self.faces:    
            print(i+",",end="")

    # The result of each flip
    def out_come(self):
        i=0
        lis=[]
        while i<=len(self.faces):
            for j in range(self.quantity):
                num=random.randint(0,len(self.faces)-1)
                lis.append(self.faces[num])
            if lis not in self.pos:
                self.pos.append(lis)
                lis=[]
            elif len(self.pos)==pow(2,self.quantity):
                break   
            else:
                i=i-1
                lis=[]
                continue        
        return self.pos                
        
    def experiment(self,N):
        M=0
        ans=0
        for j in range(N):
            result=self.out_come()
            for i in result:
                obj=i.count("Head")
                if obj>=1:
                  M=M+1      
            ans=ans+(M/(pow(2,self.quantity)))
            M=0        
        print("\nProbablity="+str(ans/N))                   
          

flip_1=flips(3,"Head","Tails")
flip_1.create_list()
flip_1.experiment(10)