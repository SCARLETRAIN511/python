#python3

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.right = None
        self.left = None


class Solution:
    def __init__(self):
        self.total = 0
    
    def convertBST(self,root):
        if root is not None:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root

    #use iteration
    def convertBST2(self,root):
        total = 0
        node = root
        stack = []
        while stack or node is not None:
            while node is not None:
                stack.append(node)
                node = node.right
            node = stack.pop()
            total += node.val
            node.val = total
            node = node.left
        
        return node
