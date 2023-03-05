class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        start, end = 0, 0
        sum = 0
        minimum = n+1
        while end < n:
            if sum >= target:
                minimum = min(minimum, end - start)
                sum -= nums[start]
                start += 1
            else:
                sum += nums[end]
                end += 1
        while start < n and sum >= target:
            minimum = min(minimum, end - start)
            sum -= nums[start]
            start += 1
        if minimum == n+1:
            return 0
        return minimum