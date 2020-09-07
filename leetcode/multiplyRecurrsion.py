#python3

class Solution:
    def multiply(self,A,B) -> int:
        #without using the * char
        if B == 1:
            return A
        if B == 0:
            return 0
        if B & 1:
            return self.multiply(A<<1,B>>1) + A
        else:
            return self.multiply(A<<1,B>>1)