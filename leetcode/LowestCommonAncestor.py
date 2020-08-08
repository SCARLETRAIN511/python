#python3

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.right = None
        self.left = None
    

class Solution:

    #use recursion
    def lowestCommonAncestor(self,root,p,q):
        parenVal = root.val
        pVal = p.val
        qVal = q.val

        if pVal > parenVal and qVal > parenVal:
            return self.lowestCommonAncestor(root.right,p,q)
        elif pVal < parenVal and qVal < parenVal:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return root

    #use iteration
    def lowestCommonAncestor2(self,root,p,q):
        pVal = p.val
        qVal = q.val

        node = root

        while node:
            parentVal = node.val
            if pVal > parentVal and qVal > parentVal:
                node = node.right
            elif pVal < parentVal and qVal < parentVal:
                node = node.left
            else:
                return node
    