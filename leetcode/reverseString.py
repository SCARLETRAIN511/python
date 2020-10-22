#python3

class Solution:
    def reverseString(self,s) -> None:
        #input is the list
        l,r = 0, len(s)-1
        while l < r:
            s[l],s[r] = s[r],s[l]
            l += 1
            r -= 1

if __name__ == "__main__":
    s = Solution()
    nums = ['r','e','v']
    print(s.reverseString(nums))
    print(nums)