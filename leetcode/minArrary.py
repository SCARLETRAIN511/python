class Solution:
    def minArray(self,numbers) -> int:
        low = 0
        high = len(numbers) - 1
        while low < high:
            pivot = (high + low) // 2
            if numbers[pivot] < numbers[high]:
                high = pivot
            elif numbers[pivot] > numbers[high]:
                low = pivot + 1
            else:
                high -= 1
        return numbers[low]


#typical bisection method

if __name__ == "__main__":
    s = Solution()
    print(s.minArray([4,5,1,2,3]))