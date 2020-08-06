#python3
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self,root):
        if not root:
            return 0
        children = [root.left,root.right]
        if not any(children):
            return 1
        min_Depth = float('inf')
        for c in children:
            if c:
                min_Depth = min(self.minDepth(c),min_Depth)
        return min_Depth + 1


