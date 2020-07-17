#from leetcode
#python3

#无重复字符串的最长子串
class solution:
    #bulk solution 
    def lengthOfLongestString(self,s:str) -> int:
        #s is the string
        stringLength = []
        stringLetter = []
        lengthOfString = 0
        for i in range(len(s)):
            if s[i] in stringLetter:
                stringLength.append(lengthOfString)
                lengthOfString = 0
            else:
                stringLetter.append(s[i])
                lengthOfString += 1
        return max(stringLength)

    def lengthOfLongestString2(self,s:str) -> int:
        k,res,cDict = -1,0,{}
        #i is the index and c is the string char in the string
        for i,c in enumerate(s):
            if c in cDict and cDict[c] >k:
                k = cDict[c]
                cDict[c] = i
            else:
                cDict[c] = i
                #use this to store the maximum length
                res = max(res,i-k)
        return res
    
    def lengthOfLongestString3(self,s:str) -> int:
        #use set to check the char, when the left pointer moves 1 block, one char should be deleted in the set and when the right pointer
        #moves to right, one char should be added to the set here.
        occ = set()
        n = len(s)
        #initialize the length as 0
        rk,ans = -1,0
        #rk is the right side pointer and have not moved
        #rk 是字串结束位置
        for i in range(n):
            if i != 0:
                occ.remove(s[i-1])
            while rk + 1 < n and s[rk + 1] not in occ:
                occ.add(s[rk+1])
                rk += 1

            ans = max(ans,rk-i+1)
        return ans

        
def main():
    s = solution()
    print(s.lengthOfLongestString2("abbacbabcd"))

if __name__ == "__main__":
    main()