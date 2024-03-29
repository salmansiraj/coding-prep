class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, len(dp)):
                dp[i] = min(dp[i], 1 + dp[i - coin])

        if dp[-1] == float('inf'):
            return -1
        return dp[-1]
