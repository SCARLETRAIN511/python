#python3

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    nodeList = []
    
    def inorderTraversal(self,root):
        if root == None:
            return
        self.inorderTraversal(root.left)
        self.nodeList.append(root.val)
        self.inorderTraversal(root.right)
    
    def helper(self,root):
        self.inorderTraversal(self,root)
        return self.nodeList
    

class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        nodeList = []
        def inorderTraversalHelper(root):
            if root == None:
                return
            inorderTraversalHelper(root.left)
            nodeList.append(root.val)
            inorderTraversalHelper(root.right)
    
        inorderTraversalHelper(root)
        return nodeList