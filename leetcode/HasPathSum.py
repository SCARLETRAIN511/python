#python3
from collections import deque

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.right = None
        self.left = None
    

class Solution:
    #Use the BFS algorithms
    def hasPathSum(self,root,sum) -> bool:
        if not root:
            return False
        queNode = deque([root])
        queVal = deque([root.val])
        while queNode:
            now = queNode.popleft()
            temo = queVal.popleft()
            if not now.left and not now.right:
                if temp == sum:
                    return True
                continue
            if now.left:
                queNode.append(now.left)
                queVal.append(now.left.val + temp)
            if now.right:
                queNode.append(now.right)
                queVal.append(now.right.val + temp)
        return False
        

        

