#python3
from collections import deque

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
    
    #BFS Algorithms
    def minDepth2(self,root):
        if not root:
            return 0
        else:
            node_deque = deque([(1,root),])

        while node_deque:
            depth, root = node_deque.popleft()
            children = [root.left,root.right]
            if not any(children):
                return depth
            for c in children:
                if c:
                    node_deque.append((depth + 1,c))

    #dfs algorithms using iterations
    def minDepth3(self,root):
        if not root:
            return 0 
        else:
            stack,minDepth = [(1,root)],float("inf")
        while stack:
            depth,root = stack.pop()
            children = [root.left,root.right]
            if not any(children):
                if c:
                    stack.append((depth + 1,c))
        return minDepth
        


