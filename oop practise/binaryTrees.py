#implemention of binary trees

class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)


def binaryTreeOp():
    tree1 = BinaryTree(1)
    print(tree1.root.value)


if __name__ == "__main__":
    binaryTreeOp() 