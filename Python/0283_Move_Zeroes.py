class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Time Complexity: O(N)
        # Space Complexity: O(1)
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != 0:
                if fast != slow:
                    nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1