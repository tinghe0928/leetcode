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




def solution(mylist):
    min_num = mylist[0]
    result = 0
    for i in mylist:
        min_num = min(min_num, i)
        result = max(result, i - min_num)
    return result


mylist=[6,2,8,10,1]
print(solution(mylist))