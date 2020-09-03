#python3

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBst(self,root,L:int,R:int) -> int:
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)
        self.ans = 0
        dfs(root)
        return self.ans

    #use iteration 
    def rangeSUmBst2(self,root,L,R) -> int:
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    ans += node.val
                if L < node.val:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
        return ans
        