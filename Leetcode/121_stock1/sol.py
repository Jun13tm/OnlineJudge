class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0
        
        ret = 0
        mi = prices[0]
        
        for i in range(1, len(prices)):
            ret = max(prices[i] - mi, ret)
            mi = min(prices[i], mi)
        return ret