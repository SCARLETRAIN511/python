#python3
#sum of 3 numbers to check if it can be 0;

class Solution:
    def threeSum(self,nums):
        #return a list with the item of list

        #先排序
        nums.sort()
        n = len(nums)
        #create the list
        ans = list()
        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                #需要和上次枚举的数不一样
                continue
            third = n - 1

            #set the target number
            target = -nums[first]
            for second in range(first + 1,n):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    #需要和上次枚举的数不一样
                    continue
                while second < third and nums[second] + nums[third] > target:
                    #如果数太大，减小third的数
                    third -= 1
                if second == third:
                    #if second and third meet, this number can not form, move to the next first number
                    break
                if nums[second] + nums[third] == target:
                    #found the number
                    
                    ans.append([nums[first],nums[second],nums[third]])
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([1,2,3,-1,-4,0]))
