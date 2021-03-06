#this script has algorithms and data structure related to trees

#Node 是组成树的基本部分
#Edge 是租成数的另一个基本部分
#Root 没有入边的节点 由边依次链接到一起的有序列表是路径

#Children, Parent, 子节点和父节点, Silbling（同一个父节点）, subtree(一个节点何其所有节点)

mytree = ['a',
        ['b',
        ['d',[],[]],
        ['e',[],[]]],
        ['c',
        ['f',[],[]],
        []]]

def BinaryTree_function(r):#r is the roor
    return [r,[],[]]

def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])
    return root

def insertRight(root, newBranch):
    t = root.pop()
    if len(t) > 0:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,t,[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]


#USING linkedlist to realize tree
#创建二叉树
class BinaryTree():
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.righChild = None
    
    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
        
    def insertRight(self,newNode):
        if self.righChild == None:
            self.righChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.leftChild
            self.leftChild = t
    
    def getRightChild(self):
        return self.righChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj
    
    def getRootVal(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.righChild:
            self.righChild.preorder()
         
        
if __name__ == "__main__":
    #initiate the binary tree
    r = BinaryTree('a')
    r.insertLeft('b')
    r.insertRight('c')
    r.getLeftChild().setRootVal('hello')
    r.getLeftChild().insertRight('d')
    print(r.getLeftChild().getRootVal())#same as below
    print(r.getLeftChild().key)


