#python3
#implementation of postordertraversal in the bst

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self,root):
        nodeList = []
        def postorderTraversalHelper(root):
            if root == None:
                return 

            postorderTraversalHelper(root.left)
            postorderTraversalHelper(root.right)
            nodeList.append(root.val)
        postorderTraversalHelper(root)
        return nodeList
