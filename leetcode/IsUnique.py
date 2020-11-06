#python3

class Solution:
    def isUnique(self,astr:str) -> bool:
        mark = 0
        for char in astr:
            moveBit = ord(char) - ord("a")
            if (mark & (1 << moveBit)) != 0:
                return False
            else:
                mark |= (1<<moveBit)
        
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isUnique("hell0"))