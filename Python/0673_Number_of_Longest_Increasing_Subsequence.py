class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time Complexity: O(N^2)
        # Space Complexity: O(N)
        n = len(nums)
        dp = [(1,1)] * n

        max_length = 1

        for i in range(1, n):
            for j in range(i-1, -1, -1):
                if nums[i] > nums[j]:
                    if dp[i][0] < dp[j][0] + 1:
                        dp[i] = (dp[j][0] + 1, dp[j][1])
                    elif dp[i][0] == dp[j][0] + 1:
                        dp[i] = (dp[i][0], dp[i][1] + dp[j][1])
            
            max_length = max(max_length, dp[i][0])
        
        return sum(count for length, count in dp if length == max_length)