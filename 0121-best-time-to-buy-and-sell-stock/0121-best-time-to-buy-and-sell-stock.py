class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            min_price = prices[0]
            max_profit = 0

            for i in range(1, len(prices)):
                if prices[i] < min_price:
                    min_price = prices[i]
                max_profits = prices[i] - min_price
                if max_profits > max_profit:
                    max_profit = max_profits

            return max_profit
      