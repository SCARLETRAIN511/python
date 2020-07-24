#python3
#plus One

class Solution:
    def plusOne(self,digits):
        #return a list 
        length = len(digits)
        i = length - 1
        while i >= 0:
            digits[i] += 1
            digits[i] = digits[i]%10
            if digits[i] != 0:
                return digits
            i -= 1
        #if all the digits are 9 if will be 1 + n x 0
        digits = [0] * (length + 1)
        digits[0] = 1
        return digits


if __name__ == "__main__":
    s = Solution()
    print(s.plusOne([1,9,9,9]))