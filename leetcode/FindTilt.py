#python3

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.tilt = 0
    
    def fintTilt(self,root) -> int:
        self.traverse(root)
        return self.tilt

    def traverse(self,node):
        if node is None:
            return 0
        left = self.traverse(node.left)
        right = self.traverse(node.right)
        self.tilt += abs(left - right)
        return left + right + node.val