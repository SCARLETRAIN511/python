#python3

#find the number in the sorted list

class Solution:
    def searchTarget(self,nums,target):
        lp = 0
        rp = len(nums) - 1
        while lp <= rp:
            if nums[lp] == target and nums[rp] == target:
                if lp == rp:
                    return [lp,lp+1]
                else:
                    return [lp,rp]
            elif nums[lp] < target:
                lp += 1
            elif nums[rp] > target:
                rp -= 1
        return [-1,-1]

    def extremeInsetionIndex(self,nums,target,left):
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = (lo + hi)//2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid + 1
        #lo == high, thus no effects to return hi
        return lo
    
    
    def searchTarget2(self,nums,target):
        leftIdx = self.extremeInsetionIndex(nums,target,True)
        if leftIdx == len(nums) or nums[leftIdx] != target:
            return [-1,-1]
        return [leftIdx,self.extremeInsetionIndex(nums,target,False)- 1]


if __name__ == "__main__":
    s = Solution()
    print(s.searchTarget2([1,2,3,4,4,5],3))