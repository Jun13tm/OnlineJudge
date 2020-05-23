class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        li = [-1 for i in range(amount + 1)]
        for coin in coins:
            if coin < len(li):
                li[coin] = 1
        for i in range(len(li)):
            if li[i] == 1:
                continue
            curr_min = float("inf")
            for coin in coins:
                if i - coin >= 0 and li[i - coin] != -1 and li[i - coin] + 1 < curr_min:
                    curr_min = li[i - coin] + 1
            if curr_min < float("inf"):
                li[i] = curr_min
        return li[-1]