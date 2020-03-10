#this script will use tree to solve various problems

from tree1 import BinaryTree
from ds1 import Stack
#import the tree structure


def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+','-','*','/',')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+','-','*','/',')']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

import operator

def evaluate(parseTree):
    opers = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()
    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()

#tree traversals
#preorder/inorder/postorder

#use recursion to traversal tree data structure

def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.gerRightChild())

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

#priority queue FIFO
#Binary heap 队首为min heap 队尾为max heap
#完全二叉树 根节点key最小

class BinaryHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    
    def percUp(self,i):
        while i//2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                tmp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i//2
    
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i*2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i*2
            else:
                return i * 2 + 1
    
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval
    
    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        print(len(alist),i)
        while i > 0:
            print(self.heapList,i)
            self.percDown(i)
            i-=1
        print(self.heapList,i)


#二叉查找树
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size 

    def __iter__(self):
        return self.root.__iter__()
    
    def put(self,key,val):
        if self.root:
            self.__put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size += 1

    def __put(self,key,val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self.__put(key,val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
                if currentNode.hasRightChild():
                    self.__put(key,val,currentNode.rightChild)
                else:
                    currentNode.rightChild = TreeNode(key,val,parent=currentNode)
    
    def __setitem(self,k,v):
        self.put(k,v)

    def get(self,key):
        if self.root:
            res = self.__get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
    
    def __get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self.__get(key, currentNode.leftChild)
        else:
            return self.__get(key, currentNode.rightChild)
    
    def __getitem__(self,key):
        return self.get(key)
    
    def __contains__(self,key):
        if self.__get(key,self.root):
            return True
        else:
            return False
    
    def delete(self,key):
        if self.size > 1:
            nodeToRemove = self.__get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError("Error, key not in tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("Error key not in tree")

    def __delitem(self,key):
        self.delete(key)

    def remove(self,currentNode):
        if currentNode.isleaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChild():
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else:
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.parent
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,currentNode.leftChild.payload,currentNode.leftChild.leftChild,currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,currentNode.rightChild.payload,currentNode.rightChild.leftChild,currentNode.rightChild.rightChild)
                    


class TreeNode:
    def __init__(self,key,val,left = None,right = None, parent = None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild
    
    def hasRightChild(self):
        return self.rightChild
    
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent
    
    def isleaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild
    
    def hasBothChild(self):
        return self.rightChild and self.leftChild
    
    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

    def findSuccessor(self):
        succ = None
        succ = self.rightChild.findMin()
        return succ
    
    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def spliceOut(self):
        if self.isleaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent



