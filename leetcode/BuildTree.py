#Python3

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self,preorder,inorder):
        self.dic = {}
        self.po = preorder
        for i in range(len(inorder)):
            self.dic[inorder[i]] = i
        return self.recur(0,0,len(inorder)-1)
    
    def recur(self,preRoot,inLeft,inRight):
        if inLeft > inRight:
            return
        root = TreeNode(self.po[preRoot])
        i = self.dic[self.po[preRoot]]
        root.left = self.recur(preRoot + 1,inLeft,i-1)
        root.right = self.recur(i-inLeft+preRoot + 1,i+1,inRight)
        return root
    

#use iteration
class Solution2:
    def buildTree(self,preorder,inorder):
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        length = len(preorder)
        stack = []
        stack.append(root)
        index = 0
        for i in range(1,length):
            preorderval = preorder[i]
            node = stack[-1]
            if node.val != inorder[index]:
                node.left = TreeNode(preorderval)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[index]:
                    node = stack[-1]
                    stack.pop()
                    index += 1
                node.right = TreeNode(preorderval)
                stack.append(node.right)
        return root

