#python3

class Solution:
    def hammingWeight(self,n) -> int:
        bits = 0
        mask = 1
        for i in range(32):
            if (n and mask) != 0:
                bits +=1
            mask << 1

        return bits


if __name__ == "__main__":
    s = Solution()
    print(s.hammingWeight(10000000000000000111111111111111111111111))