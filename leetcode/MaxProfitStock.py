#python3

class Solution:
    def maxProfit(self,prices) -> int:
        #prices is the list with the price
        inf = int(1e9)
        minPrice = inf
        maxProfit = 0
        for price in prices:
            maxProfit = max(price - minPrice,maxProfit)
            minPrice = min(price,minPrice)
        return maxProfit


if __name__ == "__main__":
    s = Solution()
    prices = [7,1,6,4,2,6,2]
    print(s.maxProfit(prices))