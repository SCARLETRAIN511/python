#python3

class Solution:
    def divingBoard(self,shorter,longer,k):
        #return a list
        if k == 0:
            return []
        if shorter == longer:
            return [shorter * k]
        
        lengths = [0] * (k+1)
        for i in range(k+1):
            lengths[i] = shorter *(k-i) + longer * i
        
        return lengths

if __name__ == "__main__":
    s = Solution()
    print(s.divingBoard(1,2,3))