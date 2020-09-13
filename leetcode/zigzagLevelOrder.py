#Python3

#zigzag level order 
from collections import deque

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.right = None
        self.left = None


class Solution:
    def zigzagLevelOrder(self,root):
        ret = []
        levelList = deque()

        if root is None:
            return []

        nodeQueue = deque([root,None])
        isOrderLeft = True

        while(len(nodeQueue)) > 0:
            currNode = nodeQueue.popleft()

            if currNode:
                if isOrderLeft:
                    levelList.append(currNode.val)
                else:
                    levelList.appendleft(currNode.val)
            
                if currNode.left:
                    nodeQueue.append(currNode.left)
                if currNode.right:
                    nodeQueue.append(currNode.right)
            else:
                ret.append(levelList)

                if (len(nodeQueue)>0):
                    nodeQueue.append(None)
                
                levelList = deque()
                isOrderLeft = not isOrderLeft
        
        return ret
