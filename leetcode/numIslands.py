#python3

class Solution:
    def numIslands(self,grid) -> int:
        #grid -> list[list]
        #dfs
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        
        numIslands = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == "1":
                    #once there is 1, there is an island, as the attached "land" is turned to zero by dfs
                    numIslands += 1
                    self.dfs(grid,i,j)
        
        return numIslands


    
    def dfs(self,grid,r,c):
        grid[r][c] = 0
        nr,nc = len(grid),len(grid[0])
        for x, y in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
            if 0 <= x < nr and 0 <= y <nc and grid[x][y] == "1":
                self.dfs(grid,x,y)#will not enter here if the condition is not satisfied
