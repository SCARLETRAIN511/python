#python3

#盛最多水的容器

class Solution:
    def maxArea(self,height) -> int:
        #height is the list with the bars with different height
        #the value is the y, the index + 1 is the x value;
        maxArea = 0
        #暴力解法
        for i in range(len(height)):
            for j in range(i + 1,len(height)):
                area = (j-i) * min(height[i],height[j])
                if area > maxArea:
                    maxArea = area
        
        return maxArea

    #use double pointers
    def maxArea2(self,height) -> int:
        #set the 2 pointers
        lp,rp = 0,len(height) - 1
        maxArea = 0
        while lp < rp:
            area = min(height[lp],height[rp]) * (rp - lp)
            maxArea = max(maxArea,area)
            if height[lp] <= height[rp]:
                #if the lp is smaller, we would like to change this pointer
                lp += 1
            else:
                #else change another pointer
                rp -= 1
        return maxArea


 
if __name__ == "__main__":
    s = Solution()
    print(s.maxArea2([1,8,6,2,5,4,8,3,7]))
