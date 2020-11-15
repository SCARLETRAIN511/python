#python3

class Solution:
    def uniquePathsWithObstacles(self,obstacleGrid) -> int:
        #obstacleGrid is list[list[int]]
        if obstacleGrid == None or obstacleGrid[0][0] == 1:
            return 0

        m,n = len(obstacleGrid),len(obstacleGrid[0])

        dp = [[0]*n for _ in range(m)]

        for i in range(0,m):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
                break
            else:
                dp[i][0] = 1

        for j in range(0,n):
            if obstacleGrid[0][j] == 1:
                dp[0][j] = 0
                break
            else:
                dp[0][j] = 1


        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0
        
        return dp[m-1][n-1]



if __name__ == "__main__":
    s = Solution()
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    print(s.uniquePathsWithObstacles(obstacleGrid))