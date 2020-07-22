#python3
#add binary

class Solution:
    def addBinary(self,a,b) -> str:
        return "{0:b}".format(int(a,2)+int(b,2))

if __name__ == "__main__":
    s = Solution()
    print(s.addBinary("11011","10110"))