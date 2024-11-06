class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time Complexity: O(N log(N))
        # Space Complexity: O(1)
        nums.sort()
        total = 0

        for i in range(0, len(nums), 2):
            total += nums[i]

        return total
        