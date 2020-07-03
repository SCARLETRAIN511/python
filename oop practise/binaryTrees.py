#implemention of binary trees
from Queue import Queue
from stack import Stack


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

#for in rder traversal left -> root -> right
    def inOrderPrint(self,start,traversal):
        if start:
            traversal = self.inOrderPrint(start.left,traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inOrderPrint(start.right,traversal)
        return traversal
    
#for post-order traversal left -> right -> root    
    def postOrderPrint(self,start,traversal):
        if start:
            traversal = self.postOrderPrint(start.left,traversal)
            traversal = self.postOrderPrint(start.right,traversal)
            traversal += str(start.value) + "-"
        return traversal
        
    def levelOrderTraversal(self,start):
        if start is None:
            return
        
        queue = Queue()
        queue.enqueue(start)

        traveral = ""
        while len(queue) > 0:
            traveral += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traveral

    def reverseLevelOrderPrint(self,start):
        if start is None:
            return
        
        queue = Queue()
        stack = Stack()
        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue

            stack.push(node)
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"

        return traversal

    #height of the tree
    def height(self,node):
        if node is None:
            return -1
        leftHeight = self.height(node.left)
        rightHeight = self.height(node.right)

        return 1 + max(leftHeight,rightHeight)

    



def binaryTreeOp():
    tree1 = BinaryTree(1)
    print(tree1.root.value)
    print(tree1.levelOrderTraversal(tree1.root))



if __name__ == "__main__":
    binaryTreeOp() 