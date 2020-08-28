#python3
#is palindrome

class Solution:
    def isPalindrome(self,x:int) -> bool:
        #to check whether the integer is the palindrome or not
        x = str(x)
        listInt = list(x)
        print(listInt)       
        return listInt == listInt[::-1]
    
    def isPalindrome2(self,x:int) -> bool:
        return str(x) == str(x)[::-1]



if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(121))