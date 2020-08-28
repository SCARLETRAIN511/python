#python3

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDiffinBST(self,root) -> int:
        vals = []
        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)

        vals.sort()

        return min(vals[i+1] - vals[i] for i in range(len(vals) - 1))


if __name__ == "__main__":
    s = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3= TreeNode(3)
    t4 = TreeNode(4)
    t2.left = t1
    t2.right = t3
    t3.right = t4
    print(s.minDiffinBST(t2))