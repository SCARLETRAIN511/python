#algorithms and code about the arrays in python

class Solution:
    def arrayAdvanceGame(self,array1):
        furthestReached = 0
        lastidx = len(array1) - 1
        i = 0
        while i <= furthestReached and furthestReached <= lastidx:
            furthestReached = max(furthestReached,array1[i] + i)
            i += 1
        return furthestReached >= lastidx
    

if __name__ == "__main__":
    s1 = Solution()
    print(s1.arrayAdvanceGame([1,2,3,45,210,31,4,0,1]))

