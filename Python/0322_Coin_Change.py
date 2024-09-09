class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Time Complexity: O(M*N)
        # Space Complexity: O(M)
        dp = [0] + [float('inf')] * amount 
        
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]