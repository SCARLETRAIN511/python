#python3
from collections import deque

#invert a binary tree
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.right = None
        self.left = None

class Solution:
    #using recursion
    def invertTree(self,treeNode):
        if not treeNode:
            return None

        right = self.invertTree(treeNode.right)
        left = self.invertTree(treeNode.left)
        treeNode.left = right
        treeNode.right = left
        return treeNode      
    
    #use iteration
    def invertTree2(self,treeNode):
        if not treeNode:
            return None
        q1 = []
        q1.append(treeNode)
        while (q1 != []):
            current = q1.pop()
            temp = current.left
            current.left = current.right
            current.right = temp

            if (current.left != None):
                q1.append(current.left)
            if (current.right != None):
                q1.append(current.right)
        return treeNode


if __name__ == "__main__":
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t1.left = t2
    t1.right = t3
    s = Solution()
    print(s.invertTree2(t1))