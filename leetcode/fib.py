#python3
class Solution:
    def fib(self,n):
        if n == 0:
            return 0
        dp = []
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
            dp[i] %= 1000000007
        
        return dp[n]

    def fb2(self,n):
        a,b = 0,1
        for i in range(n):
            a,b = b, a+b
        return a % 1000000007