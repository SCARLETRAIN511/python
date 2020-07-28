#python3
#sum of 3 numbers to check if it can be 0;

class Solution:
    def threeSum(self,nums):
        #return a list with the item of list

        #先排序
        nums.sort()
        n = len(nums)
        ans = list()
        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                countinue
            third = n - 1
            target = -nums[first]
            for second in range(first + 1,n):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first],nums[second],nums[third]])
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([1,2,3,-1,-4,0]))
