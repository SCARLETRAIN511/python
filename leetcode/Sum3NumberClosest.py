#python3
#find 3 number which have the sum that are closest to the target number

class Solution:
    def threeSumClosest(self,nums,target):
        nums.sort()
        n = len(nums)
        best = 100000
        
        #use this function to update the data
        def update(cur):
            #非局部变量
            nonlocal best
            if abs(cur - target) < abs(best - target):
                best = cur
        
        for i in range(n):
            #避免重复
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            #Define the second and the third number
            j,k = i + 1,n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return target
                
                #find the closest number
                update(s)
                if s > target:
                    k0 = k-1
                    while j<k0 and nums[k0] == nums[k]:
                        #避免重复
                        k0 -= 1
                    k = k0
                else:
                    #avoid repetition
                    j0 = j + 1
                    while j0 < k and nums[j0] == nums[j]:
                        j0 += 1
                    j = j0
        return best



if __name__ == "__main__":
    s = Solution()
    print(s.threeSumClosest([1,2,3,4,4],5))