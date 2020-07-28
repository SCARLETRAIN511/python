#python3
#find 3 number which have the sum that are closest to the target number

class Solution:
    def threeSumClosest(self,nums,target):
        nums.sort()
        n = len(nums)
        best = 100000
        
        #use this function to update the data
        def update(cur):
            nonlocal best
            if abs(cur - target) < abs(best - target):
                best = cur
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j,k = i + 1,n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return target
                    
                update(s)
                if s > target:
                    k0 = k-1
                    while j<k0 and nums[k0] == nums[k]:
                        k0 -= 1
                    k = k0
                else:
                    j0 = j + 1
                    while j0 < k and nums[j0] == nums[j]:
                        j0 += 1
                    j = j0
        return best



if __name__ == "__main__":
    s = Solution()
    print(s.threeSumClosest([1,2,3,4,4],5))