class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # Time Complexity: O(N*M)
        # Space Complexity: O(N)
        n = len(s)
        dp = [True] + [False] * n

        for i in range(1, n+1):
            for w in wordDict:
                if i-len(w) >= 0 and dp[i-len(w)] and s[i-len(w):i] == w:
                        dp[i] = True

        return dp[-1]