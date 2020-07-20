#remove duplicates

class Solution:
    def removeDuplicates(self,nums) -> int:
        #nums is the list with the sorted numbers.
        if len(nums) == 0:
            return 0

        i = 0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        print(nums)
        return i+1


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([1,2,3,3,3,4,4,6]))