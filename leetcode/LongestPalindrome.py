#python3

class Solution:
    def longestPalindrome(self,s:str) -> str:
        #dynamic programming
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        for l in range(n):
            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])

                else:
                    dp[i][j] = (dp[i+1][j-1] and s[i] == s[j])

                if dp[i][j] and l+1 > len(ans):
                    ans = s[i:j+1]
        return ans


class Solution2:
    def expandAroundCenter(self,s,left,right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            return left + 1, right - 1
    
    def longestPalindrome(self,s:str) -> str:
        start,end = 0,0
        for i in range(len(s)):
            left1,right1 = self.expandAroundCenter(s,i,i)
            left2,right2 = self.expandAroundCenter(s,i,i+1)
            if right1 - left1 > end-start:
                start,end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2,right2
        return s[start:end + 1]

if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("hjdhajeejahweiw"))