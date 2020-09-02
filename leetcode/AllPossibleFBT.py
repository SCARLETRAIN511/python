#python3

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
    
#for full binary tree, every node has no or 2 childs

class Solution:
    memo = {0:[],1:[TreeNode(0)]}

    def allPossibleFBT(self,N:int):
        #return the list with treeNodes.
        if N not in Solution.memo:
            ans = []
            for x in range(N):
                y = N - 1 -x
                #recursion store all the sub full binary tree

                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        bns = TreeNode(0)
                        bns.left = left
                        bns.right = right
                        ans.append(bns)
            Solution.memo[N] = ans
        
        return Solution.memo[N]
    


if __name__ == "__main__":
    s = Solution()
    print(s.allPossibleFBT(7))