class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start = 0
        product = 1
        count = 0
        for end in range(len(nums)):
            product *= nums[end]
            while start <= end and product >= k:
                product /= nums[start]
                start += 1
            count += end - start + 1
        return count