import random
class BT:
    lst=[]
    tree={}
    def __init__(self,root,low=[],high=[]):
        self.low=low
        self.high=high
        self.root=root

    def part(self):
        for i in self.lst:
            if i <self.root:
                self.low.append(i)
            elif i>self.root:
                self.high.append(i)

    def create_left(self,num):
        if self.low==[]:
            return
        if num==self.root:
            i=random.choice(self.low)
            self.low.remove(i)
            self.tree[num]=[i]
            for i in self.tree[num]:
                if i<self.root:
                    self.create_left(i)
        elif num!=self.root and len(self.low)!=0:
            count_low=0
            count_high=0
            self.tree[num]=[]
            while self.low!=[] and len(self.tree[num])<=2:
                i = random.choice(self.low)
                self.low.remove(i)
                if i<num and count_low<=1:
                    self.tree[num].insert(0,i)
                    count_low+=1
                elif i>num and count_high<=1:
                    self.tree[num].append(i)
                    count_high+=1

                for i in self.tree[num]:
                    self.create_left(i)
            return

    def create_right(self,num):
        if self.high==[]:
            return
        if num==self.root:
            i=random.choice(self.high)
            self.high.remove(i)
            self.tree[num].append(i)
            for i in self.tree[num]:
                if i >self.root:
                   self.create_right(i)
        elif num!=self.root and len(self.high)!=0:
            count_low=0
            count_high=0
            self.tree[num]=[]
            while self.high!=[] and len(self.tree[num])<=2:
                i = random.choice(self.high)
                self.high.remove(i)
                if i<num and count_low<=1:
                    self.tree[num].insert(0,i)
                    count_low+=1
                elif i>num and count_high<=1:
                    self.tree[num].append(i)
                    count_high+=1

                for i in self.tree[num]:
                    self.create_right(i)
            return

    def print_tree(self):
        for i in self.tree.keys():
            print(str(i)+":")
            for j in self.tree[i]:
                print ("  "+str(j))

    def insert(self,val):
        self.tree={}
        self.part()
        if val<self.root:
            self.low.append(val)
        else:
            self.high.append(val)
        self.create_left(self.root)
        self.create_right(self.root)

    def pre_order(self):
        lst=[]
        for i in self.tree.keys():
            lst.append(i)
        print(lst)

    def post_order(self):
        lst=[]
        for i in self.tree.keys():
              if i!=self.root:
                 lst.append(i)
        lst.append(self.root)
        print(lst)

    def in_order(self):
        lst=[]
        count=0
        for i in self.tree.keys():
            if i>self.root and count<1:
                lst.append(self.root)
                count+=1
            if i !=self.root:
               lst.append(i)
        print(lst)





Binary_tree=BT(27)
Binary_tree.lst=[12,34,28,11,10,65,56]
Binary_tree.part()
Binary_tree.create_left(Binary_tree.root)
Binary_tree.create_right(Binary_tree.root)
Binary_tree.insert(13)
#print(Binary_tree.tree)
Binary_tree.in_order()

