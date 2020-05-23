import random 
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0 and coins is None:
            return 1
        dp = [0] * (amount + 1)
        dp[0] = 1 
        
        random.shuffle(coins)
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]