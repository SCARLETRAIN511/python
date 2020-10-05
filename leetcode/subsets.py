#python3

class Solution:
    def subsets(self,nums):
        #return list[list]
        ans = []
        n = len(nums)
        def helper(i,tmp):
            ans.append(tmp)
            for j in range(i,n):
                helper(j+1,tmp + [nums[j]])
        help(0,[])
        return ans


class Solution2:
    def subsets(self,nums):
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res
