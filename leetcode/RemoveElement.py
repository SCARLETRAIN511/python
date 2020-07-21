class Solution:
    #this is the bulk solution
    def removeElement(self, nums, val) -> int:
        length = len(nums)
        i = 0
        j = 0
        while j < length:
            if nums[j] == val:
                length -= 1
                value = nums[j]
                nums.pop(j)
                nums.append(value)
            else:
                j += 1
                
        print(nums)
        return length

    
    def removeElement2(self,nums,val) -> int:
        #双指针
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        print(nums)
        return i
    

if __name__ == "__main__":
    s = Solution()
    print(s.removeElement2([0,1,2,2,3,0,4,2],2))
        