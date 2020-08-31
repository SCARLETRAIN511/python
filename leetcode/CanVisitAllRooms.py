#python3
import collections


class Solution:

    #dfs method
    def canVisitAllRooms(self,rooms) -> bool:
        def dfs(x:int):
            vis.add(x)

            #非局部变量
            nonlocal num
            num += 1
            for it in rooms[x]:
                if it not in vis:
                    dfs(it)
        
        vis = set()
        n = len(rooms)
        num = 0
        dfs(0)
        return num == n

    #bfs method
    def canVisitAllRooms2(self,rooms) -> bool:
        n = len(rooms)
        num = 0
        vis = {0}
        que = collections.deque([0])

        while que:
            x = que.popleft()
            num += 1
            for it in rooms[x]:
                if it not in vis:
                    vis.add(it)
                    que.append(it)
        
        return num == n


if __name__ == "__main__":
    s = Solution()
    print(s.canVisitAllRooms2([[1,2],[3,4],[0,2],[1,4],[2,3]]))