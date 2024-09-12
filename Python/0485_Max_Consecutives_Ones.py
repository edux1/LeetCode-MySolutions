class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time Complexity: O(N)
        # Space Complexity: O(1)
        cnt = 0
        max_consecutives = 0
        for n in nums:
            if n == 1:
                cnt += 1
                max_consecutives = max(cnt, max_consecutives)
            else:
                cnt = 0
        return max_consecutives