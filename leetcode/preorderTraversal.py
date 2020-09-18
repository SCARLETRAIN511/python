#python3

class TreeNode:
    def __init(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self,root):
        nodeList = []
        def preorderTraversalHelper(root):
            if root == None:
                return
            nodeList.append(root.val)
            preorderTraversalHelper(root.left)
            preorderTraversalHelper(root.right)
        preorderTraversalHelper(root)
        return nodeList

        