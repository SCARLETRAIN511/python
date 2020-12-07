#python3

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self,root):
        rightMost = dict()
        maxDepth = -1
        stack = [(root,0)]
        while stack:
            node,depth = stack.pop()
            if node is not None:
                maxDepth = max(maxDepth,depth)
                rightMost.setdefault(depth,node.val)

                stack.append((node.left,depth+1))
                stack.append((node.right,depth+1))
                
        return [rightMost[depth] for depth in range(maxDepth+1)]

