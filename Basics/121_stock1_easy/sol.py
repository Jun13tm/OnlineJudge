class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        curr = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > curr:
                if prices[i] - curr > max_profit:
                    max_profit = prices[i] - curr 
            else:
                curr = prices[i]
        return max_profit