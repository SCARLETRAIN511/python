#python3

class Solution:
    def uniquePaths(self,m,n) -> int:
        #in the grid with m rows, n columns;
        cur = [1] * n
        pre = [1] * n
        for i in range(1,m):
            for j in range(1,n):
                cur[j] = pre[j] + cur[j-1]
            pre = cur[:]

        return pre[-1]


class Solution:
    def uniquePaths(self,m,n):
        dp =[[1]*n] + [[1] + [0] * (n-1) for _ in range(m-1)]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]