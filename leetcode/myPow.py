#python3

class Solution:
    def myPow(self,x,n) -> float:
        if x == 0:
            return 0
        res = 1
        if n < 0:
            x,n = 1/x,-n
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.myPow(5,3)) 