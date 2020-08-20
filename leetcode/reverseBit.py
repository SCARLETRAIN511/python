#python3

class Solution:
    def reverseBits(self,n):
        ret,power = 0,31
        while n:
            ret += (n & 1) << power
            n = n>> 1
            power -= 1
        return ret
