#python3

class TreeNode:
    def __init__(self,x):
        self.val = x

class Solution:
    def isBalancedTree(self,root):
        if (root == None):
            return True
        return abs(self.height(root.left)-self.height(root.right)) < 2 and self.isBalancedTree(root.right) and self.isBalancedTree(root.left)

    
    def height(self,root):
        if not root:
            return -1
        return 1 + max(self.height(root.left),self.height(root.right))