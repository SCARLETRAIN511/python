#python3

class Solution:
    def getLeastNumbers(self,arr,k):
        #return list
        arr.sort()
        return arr[:k]

if __name__ == "__main__":
    arr = [1,2,423,1131,212,57,54]
    s = Solution()
    print(s.getLeastNumbers(arr,3))
        