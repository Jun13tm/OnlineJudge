class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0
        
        su = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                su += (prices[i] - prices[i - 1])
        return su