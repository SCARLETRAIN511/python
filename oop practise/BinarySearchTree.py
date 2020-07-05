#implemention of binary search tree

class Node:
    def __init__(self,data):
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self,root):
        self.root = Node(root)
    
    def insert(self,newVal):
        self.insertHelper(self.root,newVal)

    def insertHelper(self,current,newVal):
        if current.data < newVal:
            if current.right:
                self.insertHelper(current.right,newVal)
            else:
                current.right = Node(newVal)
        else:
            if current.left:
                self.insertHelper(current.left,newVal)
            else:
                current.left = Node(newVal)
