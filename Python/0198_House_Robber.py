class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        else:
            arr = nums[0:2]
            arr.append(nums[0] + nums[2])
            for i in range(3, len(nums)):
                arr.append(max(arr[i-2], arr[i-3]) + nums[i])
            return max(arr[-1], arr[-2])