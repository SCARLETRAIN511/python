#python3
#climb stairs

class Solution:
    def climbStairs(self,n:int) -> int:
        #输入层数，可以爬一层或两层
        #dynamic programming
        if (n < 2):
            return n
        i1 = 1
        i2 = 2
        for i in range(3,n+1):
            temp = i1 + i2
            i1 = i2
            i2 = temp
        
        return i2


if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(45))