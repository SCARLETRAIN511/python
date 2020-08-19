#python3

class Solution:
    def rotate(self,nums,k) -> None:
        #nums is the list with numbers in it
        for i in range(k):
            nums.insert(0,nums.pop())
        print(nums)
    
    def rotate2(self,nums,k) -> None:
        a = [0]*len(nums)
        print(a)

        for i in range(len(nums)):
            a[(i + k) % len(nums)] = nums[i]
        
        for i in range(len(nums)):
            nums[i] = a[i]
        print(nums)


if __name__ == "__main__":
    s = Solution()
    s.rotate2([1,2,3,4,5],3)