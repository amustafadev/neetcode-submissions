class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy, profit = prices[0], 0
        for i in range(1, len(prices)):
            price = prices[i]
            profit = max(profit, price - minBuy)
            minBuy = min(minBuy, price)
        return profit
