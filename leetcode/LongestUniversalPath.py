#python3

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestUniversalValuePath(self,root) -> int:
        self.ans = 0
        def arrowLength(node):
            if not node:
                return 0
            leftLength = arrowLength(node.left)
            rightLength = arrowLength(node.right)
            leftArrow = rightArrow = 0
            if node.left and node.left.val == node.val:
                leftArrow = leftLength + 1
            if node.right and node.right.val == node.val:
                rightArrow = rightLength + 1
            
            self.ans = max(self.ans,leftArrow + rightArrow)
            return max(leftArrow,rightArrow)
        
        arrowLength(root)
        return self.ans