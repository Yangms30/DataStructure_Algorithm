class Solution:
    def maxProfit(self,prices):
        if len(prices) < 2 or not prices : return 0
        minimum = float('inf')
        profit = 0
        for i in range(len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            else:
                im = prices[i] - minimum
                if(im > profit):
                    profit = im
        return profit