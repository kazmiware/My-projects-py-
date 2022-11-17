class linked_list:
    def __init__(self,last_node=None,head=None,node=None):
        self.head=head
        self.node=node
        self.last_node=last_node

    def add_item(self,item):
        if self.head==None:
            self.head=Node(item)
        elif self.node==None:
            self.node=Node(item)
            self.head.next=self.node
            self.last_node=self.node
        else:
            self.last_node.next=Node(item)
            self.last_node=self.last_node.next


    def print_list(self):
        itr=self.head
        while True:
            if itr==None:
                return
            print(itr.val,end='')
            if itr.next!=None:
                print("-->",end='')
            itr=itr.next

    def add_at(self,item,index):
        count=0
        element=self.head
        while True:
            if count==index-1:
                item=Node(item)
                item.next=element.next
                element.next=item
                break
            element=element.next
            count+=1

    def add_beginning(self,item):
        item=Node(item)
        item.next=self.head
        self.head=item
        return


class Node:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next



ll=linked_list()
ll.add_item(3)
ll.add_item(7)
ll.add_item(9)
ll.add_item(5)
ll.add_at(6,1)
ll.add_at(10,4)
ll.add_beginning(0)
ll.print_list()
