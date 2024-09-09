class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Time Complexity: O(N^2)
        # Space Complexity: O(N)
        dp = [0] * (n+1)
        dp[1] = 1

        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]