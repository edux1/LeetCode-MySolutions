class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time Complexity: O(N)
        # Space Complexity: O(1)
        if nums[0] >= nums[1]:
            largest = 0
            second_largest = 1
        else:
            largest = 1
            second_largest = 0
        for i in range(2, len(nums)):
            if nums[i] >= nums[largest]:
                second_largest = largest
                largest = i
            elif nums[i] > nums[second_largest]:
                second_largest = i

        if nums[largest] >= nums[second_largest] * 2:
            return largest
        return -1