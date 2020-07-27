#python3

#盛最多水的容器

class Solution:
    def maxArea(self,height) -> int:
        #height is the list with the bars with different height
        #the value is the y, the index + 1 is the x value;
        maxArea = 0
        for i in range(len(height)):
            for j in range(i + 1,len(height)):
                area = (j-i) * min(height[i],height[j])
                if area > maxArea:
                    maxArea = area
        
        return maxArea


if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))
