#python3

class Solution:
    def searchInsert(self,nums,target) -> int:
        low = 0
        high = len(nums)- 1
        while low < high:
            mid = low + high // 2
            if nums[mid] < target:
                low  = mid + 1
            else:
                high = mid
        return low

if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert([1,3,4,5],0))