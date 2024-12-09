class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return max(j - k for j,k in zip(prices, accumulate(prices,min)))
