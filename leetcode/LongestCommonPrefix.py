#python
#algorithms for the leetcode longest Common prefix

#only a-z chars for the input
#找出最长公共前缀

class Solution:
    def longestCommonPrefix(self,strs) -> str:
        #strs is the list
        if not strs:
            return ""
        #the first str is the assumed prefix and count is the length here
        prefix,count = strs[0],len(strs)
        for i in range(1,count):
            prefix = self.lcp(prefix,strs[i])
            if not prefix:
                break
        return prefix
    
    def lcp(self,str1,str2):
        #this function will compare 2 strs and find the longest common prefix
        length, idx = min(len(str1),len(str2)),0
        while idx < length and str1[idx] == str2[idx]:
            idx += 1
        return str1[:idx]

if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["leet","leetcode","leets","lee"]))