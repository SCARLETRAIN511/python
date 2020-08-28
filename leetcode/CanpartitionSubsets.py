#python3

class Solution:
    def canPartitionKSubsets(self,nums,k) -> bool:
        #divide into k subsets
        #divmod return the tuple with result and remainder(a//b,a%b)
        target,rem = divmod(sum(nums),k) #calculate the sum for one subset
        if rem:
            return False
        
        def search(groups):
            if not nums:
                return True
            v = nums.pop()
            for i,group in enumerate(groups):
                if group + v < target:
                    groups[i] += v
                    if search(groups):
                        return True
                    groups[i] -= v
                if not group:
                    break
            nums.append(v)
            return False
            