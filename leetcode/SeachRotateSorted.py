#python3

#bisection method

class Solution:
    def search(self,nums,target) -> int:
        #nums is the sorted list that has been rotated.
        if not nums:
            return -1
        l,r = 0,len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    #if in this range, find the number in the sorted left half
                    r = mid - 1
                else:
                    #if it is not in this range, find the number in the right half
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

if __name__ == "__main__":
    s = Solution()
    print(s.search([4,5,6,1,2,3],1))