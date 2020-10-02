#python3

class Solution:
    def ditributeCandies(self,candies:int,numOfChildren:int):
        #return a list
        candiesList = [0] * numOfChildren
        i = 0
        while candies > 0:
            candiesList[i % numOfChildren] += min(i+1,candies)
            candies -= min(i+1,candies)
            i += 1
        
        return candiesList

if __name__ == "__main__":
    s = Solution()
    print(s.ditributeCandies(15,3))
    
