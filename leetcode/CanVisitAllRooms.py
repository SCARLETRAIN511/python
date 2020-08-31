#python3

class Solution:
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