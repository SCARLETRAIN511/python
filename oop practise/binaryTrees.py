#implemention of binary trees

class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)


#we have 3 types to traverse a binary tree:
#pre order ; in order ; post order

#for pre-order root - left - right
    def preorderPrint(self,start,traversal):
        if start:
            traversal += str(start.value + '-')
            traversal = self.preorderPrint(start.left, traversal)
            traversal = self.preorderPrint(start.right, traversal)
        return traversal


def binaryTreeOp():
     tree1 = BinaryTree(1)
    print(tree1.root.value)



if __name__ == "__main__":
    binaryTreeOp() 