#python3

class Solution:
    def findRepeatNumber(self,nums) -> int:
        #find any repeat number in nums
        tempSet = set()
        repeat = -1
        for i in range(len(nums)):
            tempSet.add(nums[i])
            if len(tempSet) < i + 1:
                repeat = nums[i]
                break
        return repeat

if __name__ == "__main__":
    s = Solution()
    nums = [1,3234,4,3,3,41,52,1]
    print(s.findRepeatNumber(nums))