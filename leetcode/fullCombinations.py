#this is the full combinations for the lists given

#回溯算法

class Solution:
    def permute(self,nums):
        #return the list containing the list
        def dfs(nums,size,depth,path,used,res):
            if depth == size:
                res.append(path[:])
            
            for i in range(size):
                if not used[i]:
                    used[i] == True
                    path.append(nums[i])

                    dfs(nums,size,depth + 1,path,used,res)
                    used[i] = False
                    path.pop()
        size = len(nums)
        if len(nums) == 0:
            return []
        used = [False for _ in range(size)]
        res = []
        dfs(nums,size,0,[],used,res)
        return res
        
