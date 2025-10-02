from math import inf

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0 and dp[i - coin] != inf:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[amount] == inf else dp[amount]
        
