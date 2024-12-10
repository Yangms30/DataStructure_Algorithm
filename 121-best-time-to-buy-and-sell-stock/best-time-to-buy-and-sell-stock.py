class Solution:
    def maxProfit(self,prices):
        if not prices or len(prices) < 2:
            return 0
        min_price = float('inf')  # Set initial minimum price to infinity
        max_profit = 0  # Initialize maximum profit as 0
        for price in prices:
        # Update the minimum price seen so far
            if price < min_price:
                min_price = price
        # Calculate the profit if sold today and update the maximum profit
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit