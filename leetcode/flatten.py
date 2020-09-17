#python3

#turn the binary tree into a linkedlist

class TreeNoe:
    def __init__(self,val = 0,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self,root) -> None:
        '''
        do not return anything
        '''
        preorderList = list()
        def preorderTraversal(root):
            if root:
                preorderTraversal(root.left)
                preorderTraversal(root.right)
        
        preorderTraversal(root)
        size = len(preorderList)

        for i in range(1,size):
            prev,curr = preorderList[i-1],preorderList[i]
            prev.left = None
            prev.right = None