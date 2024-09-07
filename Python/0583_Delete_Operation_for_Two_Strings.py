class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # Time Complexity: O(M*N)
        # Space Complexity: O(M*N)
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m + 1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        lcs = dp[m][n]
        return (m-lcs) + (n-lcs)