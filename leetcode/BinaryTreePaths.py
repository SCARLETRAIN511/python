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
    
    
    def binaryTreePaths2(self,root):
        if not root:
            return []
        
        paths = []
        stack = [(root,str(root.val))]
        while stack:
            node,path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path + "->" + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + "->" + str(node.right.val)))
        return paths


if __name__ == "__main__":
    s = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t1.right = t2
    t1.left = t3
    print(s.binaryTreePaths2(t1))

