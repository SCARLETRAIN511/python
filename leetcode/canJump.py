#python3

class Solution:
    def canJump(self,nums) -> bool:
        n,rightMost = len(nums),0
        for i in range(n):
            if i <= rightMost:
                rightMost = max(rightMost,i + nums[i])
                if rightMost >= n - 1:
                    return True
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.canJump([3,2,1,0,4]))