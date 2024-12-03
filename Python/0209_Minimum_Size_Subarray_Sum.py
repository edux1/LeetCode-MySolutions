class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # Time complexity: O(n)
        # Space complexity: O(1)

        n = len(nums)
        left = 0
        min_length = n+1
        
        for right in range(n):
            target -= nums[right]

            while target <= 0:
                min_length = min(min_length, right - left + 1)
                target += nums[left]
                left += 1
        
        return min_length if min_length <= n else 0