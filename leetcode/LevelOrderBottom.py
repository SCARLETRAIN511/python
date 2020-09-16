#python3

#levelOrderBottom
import collections

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.right = None
        self.left = None


class Solution:
    def levelOrderBottom(self,root):
        levelOrder = list()
        if not root:
            return levelOrder
        
        q = collecionts.deque([root])

        while q:
            level = list()
            size = len(q)
            for i in range(size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            levelOrder.append(level)
        return levelOrder[::-1]
