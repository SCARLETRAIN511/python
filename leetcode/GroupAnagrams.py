#python3
import collections

class Solution:
    def groupAnagrams(self,strs):
        #return a list with lists
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

    #second type
    def groupAnagrams2(self,strs):
        tempDict = {}
        for tempStr in strs:
            sortStr = self.HashMapFunc(tempDict)
            if sortStr in tempDict:
                tempDict[sortStr].append(tempStr)
            else:
                tempDict[sortStr] = [tempStr]
        return list(tempDict.values())

        
    def HashMapFunc(self,tempStr):
        return ''.join(sorted(list(tempStr)))



class Solution2:
    def groupAnagrams(self,strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1

            ans[tuple(count)].append(s)
        return ans.values()

    def groupAnagrams2(self,strs):
        tempDict = {}
        for tempStr in strs:
            sortStr = self.HashMapFunc(tempStr)
            if sortStr in tempDict:
                tempDict[sortStr].append(tempStr)
            else:
                tempDict[sortStr] = [tempStr]
        return list(tempDict.values())


    def HashMapFunc(self,tempStr):
        key = [0] * 26
        for char in tempStr:
            key[ord(char) - ord('a')] += 1
        return ''.join([str(i) for i in key])


if __name__ == "__main__":
    s = Solution2()
    print(s.groupAnagrams2(["are","ear","bat","tab"]))