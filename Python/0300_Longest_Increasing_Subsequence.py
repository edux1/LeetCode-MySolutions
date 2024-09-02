class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time Complexity: O(N^2)
        # Space Complexity: O(N)
        n = len(nums)
        dp = [1] * (n)

        for i in range(1, n):
            for j in range(i-1, -1, -1):
                if nums[i] > nums[j] and dp[i] <= dp[j]:
                    dp[i] = dp[j] + 1

        return max(dp)