#python3

class Solution:
    def rotate(self,nums,k) -> None:
        #nums is the list with numbers in it
        for i in range(k):
            nums.insert(0,nums.pop())
        print(nums)


if __name__ == "__main__":
    s = Solution()
    s.rotate([1,2,3,4,5,],3)