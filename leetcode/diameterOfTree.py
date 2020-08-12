#python3

#calculate the diameter of the binary tree
#the diameter of the binary tree os is the maximum length between any 2 points.


class TreeNode:
    def __init__(self,x):
        self.val = x
        self.right = None
        self.left = None


class Solution:
    def diameterOfBinaryTree(self,root) -> int:
        self.ans = 1
        def depth(root):
            if not root:
                return 0

            left = depth(root.left)
            right = depth(root.right)

            self.ans = max(self.ans,left + right + 1)
            return max(left,right) + 1
        depth(root)
        return self.ans - 1