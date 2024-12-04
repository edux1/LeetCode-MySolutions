class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Time complexity: O(n)
        # Space complexity: O(n)

        k %= len(nums)
        
        if k != 0:
            nums[:k], nums[k:] = nums[-k:], nums[:-k]