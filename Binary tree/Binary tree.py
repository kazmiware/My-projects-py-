class Binary_tree:
    def __init__(self,root,node=None):
        self.root=Node(root)
        self.node=node

    def add_node(self,item):
        itr = self.root
        while True:
            if item<itr.val:
                if itr.left==None:
                    itr.left=Node(item)
                itr=itr.left
            elif item>itr.val:
                if itr.right==None:
                    itr.right=Node(item)
                itr=itr.right
            else:
              break

    def preorder(self):
        print("Preorder Traversal:")
        print(str(self.root.val)+" --> Root Node")
        itr=self.root
        while itr.left!=None:
            print(itr.left.val)
            itr=itr.left

        itr = self.root
        while itr.right != None:
            print(itr.right.val)
            itr = itr.right

    def inorder(self):
        print("Inorder Traversal:")
        itr = self.root
        while itr.left != None:
            print(itr.left.val)
            itr = itr.left

        print(str(self.root.val) + " --> Root Node")

        itr = self.root
        while itr.right != None:
            print(itr.right.val)
            itr = itr.right

    def postorder(self):
        print("Postorder Traversal:")
        itr = self.root
        while itr.left != None:
            print(itr.left.val)
            itr = itr.left

        itr = self.root
        while itr.right != None:
            print(itr.right.val)
            itr = itr.right
        print(str(self.root.val) + " --> Root Node")

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

bt=Binary_tree(4)
bt.add_node(2)
bt.add_node(6)
bt.add_node(1)
bt.add_node(7)
bt.preorder()
bt.inorder()
bt.postorder()