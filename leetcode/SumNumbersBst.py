#python3

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
    

class Solution:
    def sumNumbers(self,root) -> int:
        #calculate the sum of all the individual path
        #eg. 1path 1->2->3, means 123;

        #dfs
        if not root:
            return 0
        stack = [(root,str(root.val))]
        res = 0

        while stack:
            #sum makes the combination of the number and transferred them to int
            node, sum = stack.pop(0)
            if node.left:
                stack.append((node.left,sum + str(node.left.val)))
            if node.right:
                stack.append((node.right, sum + str(node.right.val)))
            if not node.left and not node.right:
                res += int(sum)
        
        return

