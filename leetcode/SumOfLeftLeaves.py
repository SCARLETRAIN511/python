#python3

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.sum = 0
    def sumOfLeftLeaves(self,root) -> int:
        if root == None:
            return 0
        if (root.left != None and root.left.left == None and root.left.right == None):
            self.sum += root.left.val
        self.sumOfLeftLeaves(root.left)
        self.sumOfLeftLeaves(root.right)
        return self.sum

if __name__ == "__main__":
    s = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t1.right = t2
    t1.left = t3
    print(s.sumOfLeftLeaves(t1))