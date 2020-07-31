#python3

#find all the combinations that can add to the target, the number can be used multiple times.


class Solution:
    def combinationSum(self,candidates,target):
        size = len(candidates)
        if size == 0:
            return []
        
        candidates.sort()

        path = []
        res = []
        self.__dfs(candidates,0,size,path,res,target)
        return res
    

    def __dfs(self,candidates,begin,size,path,res,target):
        if target == 0:
            res.append(path[:])
            return
        for index in range(begin,size):
            residue = target - candidates[index]
            if residue < 0:
                break
            path.append(candidates[index])
            self.__dfs(candidates,index,size,path,res,residue)
            path.pop()
