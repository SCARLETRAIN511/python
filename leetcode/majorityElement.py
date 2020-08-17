#python3

#find the major element in the list, major element occurs more than half the size of the list

class Solution:
    def majorityElement(self,nums) -> int:
        n = len(nums)
        numsDict = dict()
        for i in nums:
            if i in numsDict.keys():
                numsDict[i] += 1
                print(numsDict[i])
            else:
                numsDict[i] = 0


if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([1,1,1,2,3]))
