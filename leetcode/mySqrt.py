#python3

class Solution:
    def mySqrt(self,x:int) -> int:
        if x == 0:
            return 0
        
        c,x0 = float(x),float(x)
        while True:
            xi = 0.5 * (x0 + c/x0)
            if abs(x0-xi) < 1e-7:
                break
            x0 = xi
        
        return int(x0)

class Solution2:
    def mySqrt(self,x:int) -> int:
        left,right,ans = 0,x,-1
        while left <= right:
            mid = (left + right)//2
            if mid * mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
                

if __name__ == "__main__":
    s = Solution2()
    print(s.mySqrt(5))