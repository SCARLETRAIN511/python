#python3
#for binary tree, write a program to check whether it is a symmetrical binary tree
#first define the treeNode

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left =None
        self.right


class Solution:
    #this method uses recursion
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.checkNode(root,root)
        
    def checkNode(self,treeNode1, treeNode2):
        if treeNode1 == None and treeNode2 == None:
            return True
        if treeNode1 == None or treeNode2 == None:
            return False

        return treeNode1.val == treeNode2.val and self.checkNode(treeNode1.left,treeNode2.right) and self.checkNode(treeNode1.right,treeNode2.left)