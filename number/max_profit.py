class Solution:

    @staticmethod
    def maxProfit_0(prices):
        maxprice = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                maxprice = max(maxprice, prices[j] - prices[i])
        return maxprice

    @staticmethod
    def maxProfit(prices):
        minprice = prices[0]
        maxprofit = 0
        for price in prices:
            minprice = min(minprice, price)
            maxprofit = max(maxprofit, price - minprice)
        return maxprofit


prices=[6,2,8,10,1]
print(Solution.maxProfit(prices))