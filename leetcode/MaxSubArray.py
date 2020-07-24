#python3
#max Sub array 最大子序和
class Solution:
    def maxSubArray(self,nums) -> int:
        #it should be successive
        maxiMum = -1000
        sumNum = 0
        for i in range(len(nums)):
            sumNum = nums[i]
            for j in range(i+1,len(nums)):
                sumNum += nums[j]
                if sumNum > maxiMum:
                    maxiMum = sumNum
        return maxiMum
    
    def maxSubArray2(self,nums) -> int:
        #dynamic programmiong
        pre = 0
        maxAns = nums[0]
        for i in nums:
            pre = max(pre + i,i);
            maxAns = max(maxAns,pre)
        return maxAns




if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray2([-1,1,2,3,4,5,10,-15]))

