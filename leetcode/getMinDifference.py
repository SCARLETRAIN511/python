#python3

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.right = None
        self.left = None


class Solution:
    def getMinimumDifference(self,root) -> int:
        st = []
        p = root
        pre = -float("inf")
        minVal = float("inf")
        while p is not None or st:
            while p is not None:
                #all the left node is in the st
                st.append(p)
                p = p.left
            p = st.pop()
            cur = p.val
            if cur - pre < minVal:
                minVal = cur - pre
            pre = cur
            p = p.right

        return minVal
