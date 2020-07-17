#python3
#is palindrome

class Solution:
    def isPalindrome(self,x:int) -> bool:
        #to check whether the integer is the palindrome or not
        x = str(x)
        listInt = list(x)
        print(listInt)
        print(listInt.reverse())
        return listInt == listInt.reverse()

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(121))