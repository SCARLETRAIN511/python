class Solution:
    def lengthOfLastWord(self,s) -> int:
        #s is the string, return the integer
        count = 0
        if (s == ""):
            return count
        lengthStr = len(s)
        if (len == 1):
            if s[0] == " ":
                return 0
            else:
                return 1
        i = lengthStr-1
        while i >= 0:
            if s[i] != " ":
                count += 1;
            if s[i] == " " and count > 0:
                break
            i -= 1
        
        return count
    
    def lengthOfLastWord2(self,s):
        return len(s.rstrip().split(" ")[-1])


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLastWord2("a ashajsh"))