class Solution(object):
    def maxProfit(self, prices):
        if len(prices) <= 1: return 0
        
        front = [0] * len(prices)
        end = [0] * len(prices)
        
        mi = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > mi:
                front[i] = max(front[i - 1], prices[i] - mi)
            else:
                front[i] = front[i - 1]
                mi = prices[i]
        
        ma = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            if prices[i] < ma:
                end[i] = max(end[i + 1], ma - prices[i])
            else:
                end[i] = end[i + 1]
                ma = prices[i]
        for i in range(len(front)):
            front[i] += end[i]
        return max(front)        