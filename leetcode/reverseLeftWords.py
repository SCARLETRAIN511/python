#python3

class Solution:
    def reverseLeftWord(self,s:str,n:int):
        #return string
        return s[n:] + s[:n]

if __name__ == "__main__":
    s = Solution()
    print(s.reverseLeftWord("Shaojiazhou",2))