#python3

class Solution:
    def sortColors(self,nums) -> None:
        #we can return the list here
        n = len(nums)
        ptr = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[ptr] = nums[ptr],nums[i]
                ptr += 1
        
        for i in range(ptr,n):
            if nums[i] == 1:
                nums[i],nums[ptr] = nums[ptr], nums[i]
                ptr += 1
        return nums

if __name__ == "__main__":
    s = Solution()
    print(s.sortColors([1,2,0,2,1,1,0]))