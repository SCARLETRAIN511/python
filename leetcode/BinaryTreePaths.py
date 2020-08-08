#python3

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.right = None
        self.left = None


class Solution:
    def binaryTreePaths(self,root):
        #return list
        def construcPaths(root,path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path += "->"
                    construcPaths(root.left,path)
                    construcPaths(root.right,path)
        paths = []
        construcPaths(root,"")
        return paths
        

