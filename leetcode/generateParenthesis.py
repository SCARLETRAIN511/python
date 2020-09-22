#python3

class Solution:
    def generateParenthesis(self,n: int,):
        #return a list
        #this program will generate a lit with all the valid combinations of brackets
        #n means the pairs of the brackets here
        def generate(A):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append("(")
                generate(A)
                A.pop()
                A.append(")")
                generate(A)
                A.pop()
        
        def valid(A):
            bal = 0
            for c in A:
                if c == "(":
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0
        ans = []
        generate([])
        return ans
    

class Solution2:
    def generateParenthesis(self,n):
        ans = []
        def backTrack(S,left,right):
            if len(S)  == 2*n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backTrack(S,left + 1,right)
                S.pop()
            if right < left:
                S.append(")")
                backTrack(S,left,right+1)
                S.pop()

        backTrack([],0,0)
        return ans
