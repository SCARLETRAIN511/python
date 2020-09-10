#python3

class TreeNode:
    def __init__(self,val,left=None,right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self,n):
        #use recursion
        def generateTrees(start,end):
            if start > end:
                return [None,]
            allTrees = []
            for i in range(start,end+1):
                leftTrees = generateTrees(start,i-1)
                rightTrees = generateTrees(i+1,end)

                for l in leftTrees:
                    for r in rightTrees:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        allTrees.append(currTree)
            return allTrees
        
        return generateTrees(1,n)if n else []


#same as the solution1, but only return the number

class Solution2:
    def numTrees(self,n) -> int:
        c = 1
        for i in range(0,n):
            c = c*2*(2*i+1)/(i+2)
        return int(c)

    def numTrees2(self,n) -> int:
        G = [0]*(n+1)
        G[0],G[1] = 1,1
        for i in range(2,n+1):
            for j in range(1,i+1):
                G[i] += G[j-1] * G[i-j]
        
        return G[n]


if __name__ == "__main__":
    s = Solution2()
    print(s.numTrees2(5))
        


