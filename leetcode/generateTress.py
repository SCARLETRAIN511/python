#python3

class TreeNode:
    def __init__(self,val,left=None,right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self,n):
        #use recursion
        def generateTrees(start,end):
            if start > end:
                return [None,]
            allTrees = []
            for i in range(start,end+1):
                leftTrees = generateTrees(start,i-1)
                rightTrees = generateTrees(i+1,end)

                for l in leftTrees:
                    for r in rightTrees:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        allTrees.append(currTree)
            return allTrees
        
        return generateTrees(1,n)if n else []

