#python3

#count the number of zeros in the factorail of a number

class Solution:
    def trailingZeroes(self,n) -> int:
        factorial = 1
        for i in range(1,n+1):
            factorial *= i

        print(factorial)
        zeroCount = 0
        while factorial % 10 == 0:
            zeroCount += 1
            factorial = factorial // 10

        return zeroCount

    def trailingZeros2(self,n) -> int:
        zeroCount = 0
        currentMultiple = 5
        while n >= currentMultiple:
            zeroCount += n // currentMultiple
            currentMultiple *= 5
        return zeroCount

if __name__ == "__main__":
    s = Solution()
    print(s.trailingZeros2(30))