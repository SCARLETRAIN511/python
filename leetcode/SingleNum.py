#Python3

#given a list, except one number, all the numbers in the list occur twice, find tthat number

class Solution:
    def singleNumber(self,nums) -> int:
        numDict = dict()
        for num in nums:
            if num not in numDict.keys():
                numDict[num] = 1
            else:
                numDict[num] += 1
        for i in numDict.keys():
            if numDict[i] == 1:
                return i
    
    def singleNum2(self,nums) -> int:
        numSet = set()
        for i in nums:
            if i not in numSet:
                numSet.add(i)
            else:
                numSet.remove(i)
        return numSet.pop()


if __name__ == "__main__":
    s = Solution()
    print(s.singleNum2([2,2,3,3,4,4,5]))