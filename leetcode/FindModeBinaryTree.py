#python3

#find the mode in the binary tree
from collections import deque
import collections

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.right = None
        self.left = None


class Solution:
    def findMode(self,root):
        modeNum = []
        if root == None:
            return modeNum
        res = []
        queue = deque()
        queue.append(root)

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        tmp = collections.Counter(res).most_common()
        for k, v in tmp:
            if v == tmp[0][1]:
                modeNum.append(k)

        return modeNum

if __name__ == "__main__":
    s = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(2)
    t4 = TreeNode(0)
    t1.right = t2
    t2.right = t3
    t1.left = t4
    print(s.findMode(t1))