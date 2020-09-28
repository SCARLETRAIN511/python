#python3
import collections


class Solution:
    def orangeRotting(self,grid) -> int:
        #for the given gird, u have the 0,1,2, 0 means no orange, 1 means fresh orange and 2 means rotten orange
        #every minute will make the fresh orange near the rotten orange rotting how many minutes will all orange rotten?
        #if not possible, return -1
        r,c = len(grid),len(grid[0])
        queue = collections.deque()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    queue.append((r,c,0))
                    #add the position of the rotten orange to the queue
        
        def neighbours(r,c):
            for nr,nc in ((r-1,c),(r,c-1),(r+1,c),(r,c+1)):
                #get the positions of the oranges around that rotten orange
                if 0 <= nr < r and 0 <=nc < c:
                    yield nr,nc#yeild can turn this function into an iterable object

        d = 0

        while queue:
            r,c,d = queue.popleft()
            for nr,nc in neighbours(r,c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr,nc,d + 1))
        
        if any(1 in row for row in grid):
            return -1
            #the condition when we still have fresh oranges

        return d

        