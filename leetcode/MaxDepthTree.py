#python3

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.right = None
        self.left = None


class Solution:
    def maxDepth(self,root) -> int:
        return self.height(root)
    
    def height(self,node):
        if node is None:
            return -1
        leftHight = self.height(node.left)
        rightHeight = self.height(node.right)

        return 1 + max(leftHight, rightHeight)