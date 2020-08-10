#python3

#find the mode in the binary tree
from collections import deque

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
        
        nums = dict()
        maxOcc = 0
        maxNum = 0
        for i in res:
            if i in nums.keys():
                nums[i] += 1
            else:
                nums[i] = 1
        print(nums)
        print(s)

        for i in nums.keys():
            if nums[i] >= maxOcc:
                maxOcc = nums[i]
                maxNum = i
        
        return [maxNum]


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