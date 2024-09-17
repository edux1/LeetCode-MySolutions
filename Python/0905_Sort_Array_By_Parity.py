class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Time Complexity: O(N)
        # Space Complexity: O(1)
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] % 2 == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        return nums