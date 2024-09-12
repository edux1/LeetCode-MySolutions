class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        # Time Complexity: O(N*M)
        # Space Complexity: O(1)
        max_wealth = 0
        for i in range(len(accounts)):
            cnt = 0
            for j in range(len(accounts[0])):
                cnt += accounts[i][j]
            max_wealth = max(cnt, max_wealth)
        return max_wealth