class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Time Complexity O(N)
        n = len(nums)

        if n == 1 or nums[0] >= n-1:
            return True
        if n == 2:
            return False

        distance_to_pos = 0

        for i in range(n-2, -1, -1):
            distance_to_pos += 1
            if nums[i] >= distance_to_pos:
                distance_to_pos = 0
            
        if distance_to_pos == 0:
            return True
        return False