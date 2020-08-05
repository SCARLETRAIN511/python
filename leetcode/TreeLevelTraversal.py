#python3

#level traversal from top and bottom for the binary tree

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self,root):
        ret = []
        if (root == None):
            return ret
        q = []
        q.append(root)
        while (len(q) != 0):
            currentLevelSize = len(q)
            ret.append([])
            for i in range(1,currentLevelSize + 1):
                node = q.pop(0)
                #为每层添加便利过节点的值
                ret[len(ret) - 1].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return ret

                
if __name__ == "__main__":
    s = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t1.right = t2
    t2.right = t3
    print(s.levelOrderBottom(t1))