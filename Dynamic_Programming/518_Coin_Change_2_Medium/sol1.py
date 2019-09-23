class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        if amount < 0 or not coins:
            return 0

        # Row: Coins, Column: Amounts)
        table = [[1] for i in range(len(coins) + 1)]
        for i in range(amount):
            table[0].append(0)
        # Ensure order
        coins.sort()

        # Fill the table row by row
        for row in range(1, len(coins) + 1):
            coin = coins[row - 1]
            for col in range(1, amount + 1):
                if col - coin >= 0:
                    su = table[row][col - coin] + table[row - 1][col]
                else:
                    su = table[row - 1][col]
                table[row].append(su)
        return table[-1][-1]