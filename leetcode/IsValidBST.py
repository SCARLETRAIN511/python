#python3

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.right = None
        self.left = None
    
class Solution:
    def isValidBST(self,root) -> bool:
        stack,inorder = [],float("-inf")
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        
        return True
    
    def isValidBST2(self,root) -> bool:
        def isValidBST(self,root):
            def helper(node,lower = float("-inf"),upper = float("inf")):
                if not node:
                    return True
                val = node.val
                if val <= lower or val >= upper:
                    return False
                
                if not helper(node.right,val,upper):
                    return False
                
                if not helper(node.left,lower,val):
                    return False
                return True
            return helper(root)
            