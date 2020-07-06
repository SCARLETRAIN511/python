#implemention of binary search tree

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

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
    
    def search(self, val):
        return self.searchHelper(self.root,val)
    
    def searchHelper(self,current,findVal):
        if current:
            if current.data == findVal:
                return True
            elif current.data < findVal:
                return self.searchHelper(current.right,findVal)
            else:
                return self.searchHelper(current.left,findVal)

    #this is a class method
    @classmethod
    def isBST(cls):
        def helper(node,lower = float("-inf"),upper = float("inf")):
            if not Node:
                return True
            val = node.data
            if val <= lower or val >= upper:
                return False
            if not helper(node.right,val,upper):
                return False
            if not helper(node.left,lower,val):
                return False
            return True
        return helper(cls.root)



def bstOp():
    bst1 = BST(10)
    bst1.insert(2)
    bst1.insert(14)
    bst1.insert(4)

    print(bst1.search(4))


if __name__ == "__main__":
    bstOp()