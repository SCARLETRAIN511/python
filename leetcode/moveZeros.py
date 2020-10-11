#python3

class Solution:
    def moveZeros(self,nums) -> None:
        if not nums:
            return 0
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[j] = nums[i]
                #count the num which is not 0
                j += 1
        
        for i in range(j,len(nums)):
            nums[i] = 0

class Solution2:
    def moveZeros(self,nums) -> None:
        if not nums:
            return 0
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[j],nums[i] = nums[i],nums[j]
                j += 1

if __name__ == "__main__":
    s = Solution()
    num1 = [1,2,43,23,45,0,42,5,0,6,0,87]
    s.moveZeros(num1)
    print(num1)
