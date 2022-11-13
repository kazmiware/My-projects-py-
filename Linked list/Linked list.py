class linked_list:

    linked_lst={}

    def __init__(self,ele=[],root=None,next=None):
        self.ele = ele
        self.root = root
        self.next = next

    def create_list(self):
        count = 0
        for i in self.ele:
            self.linked_lst[i] = count+1
            count+=1

    def add_start(self,node):
        for i ,j in self.linked_lst.items():
           self.linked_lst[i]= j+1
        self.linked_lst[node] = 1

    def add_middile(self,node,index):
        for i,j in self.linked_lst.items():
            if j>index:
                self.linked_lst[i] = j+1
        self.linked_lst[node] = index+1

    def add_end(self,node):
        self.linked_lst[node] = len(self.linked_lst)+1


    def print_ll(self):
        count = 1
        while True:
            if count not in range(len(self.linked_lst.keys()) + 1):
                break
            for i ,j in self.linked_lst.items():
                if j == count:
                    print(i,end='')
                    if count!=len(self.linked_lst):
                        print('--->',end='')
                    count+=1




l_l=linked_list([10,9,3,15])
l_l.create_list()
l_l.add_start(1)
l_l.add_middile(11,4)
l_l.add_end(20)
l_l.print_ll()



