#python3

class Solution:
    #bulk solution
    def tribonacci(self,n:int) -> int:
        def getNum(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            elif n == 2:
                return 1
            return getNum(n-1) + getNum(n-2) + getNum(n-3)
        
        return getNum(n)


class Solution2:
    
    def tribonacci(self,n):

        def helper(k):
            if k == 0:
                return 0 
            if nums[k]:
                return nums[k]
        
            nums[k] = helper(k-1) + helper(k-2) + helper(k-3)
            return nums[k]


        nums = [0] * 38
        nums[1] = nums[2] = 1
        helper(37)
        return nums[n]


if __name__ == "__main__":
    s = Solution2()
    print(s.tribonacci(5))