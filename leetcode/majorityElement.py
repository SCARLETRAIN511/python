#python3

#find the major element in the list, major element occurs more than half the size of the list

class Solution:
    def majorityElement(self,nums) -> int:
        n = len(nums)
        print(n//2)
        numsDict = dict()
        for i in nums:
            if i not in numsDict.keys():
                numsDict[i] = 1
                if numsDict[i] > n//2:
                    return i
            else:
                numsDict[i] += 1
                if numsDict[i] > n//2:
                    return i

    def majorityElement2(self,nums) -> int:
        nums.sort()
        return nums[len(nums)//2]
    
    #divide and conquer
    def majorityElement3(self,nums) -> int:
        def majorityElementRec(lo,hi):
            if lo == hi:
                return nums[lo]
            
            mid = (hi-lo) // 2 + lo
            left = majorityElementRec(lo,mid)
            right = majorityElementRec(mid + 1,hi)

            if left == right:
                return left
            
            leftCount = sum(1 for i in range(lo,hi + 1) if nums[i] == left)
            rightCount = sum(1 for i in range(lo,hi+1) if nums[i] == rihgt)

            return left if leftCount > right else right
        
        return majorityElementRec(0,len(nums) - 1)
        

if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([1]))
