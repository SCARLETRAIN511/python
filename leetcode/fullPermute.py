#python3

class Solution:
    def permute(self,nums):
        #return a list with lists
        def backTrack(first = 0):
            if first == n:
                res.append(nums[:])
            for i in range(first,n):
                nums[first],nums[i] = nums[i],nums[first]

                backTrack(first + 1)
                nums[first] ,nums[i] = nums[i],nums[first]
            
        n = len(nums)
        res = []
        backTrack()
        return res
        

if __name__ == "__main__":
    s = Solution()
    print(s.permute([1,2,3]))