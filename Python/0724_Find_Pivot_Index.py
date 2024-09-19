class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time Complexity: O(N)
        # Space Complexity: O(N)
        left_sum, right_sum = 0, sum(nums)

        for i in range(len(nums)):
            right_sum -= nums[i]
                
            if left_sum == right_sum:
                return i
            
            left_sum += nums[i]
        
        return -1