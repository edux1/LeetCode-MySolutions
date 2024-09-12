class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Time Complexity: O(N)
        # Space Complexity: O(N)
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        return nums