#python3
#check whether a string is palindrome

class Solution:
    def isPalindrome(self,s) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        print(sgood)
        n = len(sgood)
        left,right = 0,n - 1
        while left < right:
            if sgood[left] != sgood[right]:
                return False
            left,right = left + 1, right - 1
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("Hell7eH"))