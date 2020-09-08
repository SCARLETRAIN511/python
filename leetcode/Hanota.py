#python3
#implementation of hanota problem

class Solution:
    def hanota(self,A,B,C) -> None:
        n = len(A)
        self.move(n,A,B,C)
        
    def move(self,n,A,B,C):
        if n == 1:
            C.append(A[-1])
            A.pop()
            return
        
        else:
            self.move(n-1,A,C,B)
            C.append(A[-1])
            A.pop()
            self.move(n-1,B,A,C)
    

