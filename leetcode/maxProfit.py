#python3

class Solution:
    def maxProfit(self,prices) -> int:
        #you can join the trade multiple times
        #but you need to sell the stock before buying the next stock
        #prices is a list
        i = 0
        valley = prices[0]
        peak = prices[0]
        maxprofit = 0
        while (i < len(prices) - 1):
            while (i < len(prices) - 1 and prices[i] >= prices[i + 1]):
                i += 1
            valley = prices[i]
            
            while (i < len(prices) - 1 and prices[i] <= prices[i + 1]):
                i += 1
            peak = prices[i]
            
            maxprofit += (peak - valley)
        return maxprofit

class Solution2(object):
    """
    docstring
    """
    def maxProfit(self, prices) -> int:
        maxprofit = 0
        for i in range(1,len(prices)):
            if (prices[i] > prices[i-1]):
                maxprofit += prices[i] - prices[i-1]
        
        return maxprofit


if __name__ == "__main__":
    s = Solution2()
    print(s.maxProfit([7,1,5,3,6,4]))