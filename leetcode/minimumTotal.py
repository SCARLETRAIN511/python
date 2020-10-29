#python3

class Solution:
    def minimumTotal(self,triangle) -> int:
        #triangle is list[list]
        n = len(triangle)
        f = [[0]*n for _ in range(n)]
        f[0][0] = triangle[0][0]

        for i in range(1,n):
            f[i][0] = f[i-1][0] + triangle[i][0]
            for j in range(1,i):
                f[i][j] = min(f[i-1][j-1],f[i-1][j] + triangle[i][j])
            f[i][i] = f[i-1][i-1] + triangle[i][i]
        
        return min(f[n-1])
    
    def minimumTotal2(self,triangle):
        n = len(triangle)
        f = [0] * n
        f[0] = triangle[0][0]

        for i in range(1,n):
            f[i] = f[i-1] + triangle[i][i]
            for j in range(i-1,0,-1):
                f[j] = min(f[j-1],f[j]) + triangle[i][j]
            f[0] += triangle[i][0]
        
        return min(f)