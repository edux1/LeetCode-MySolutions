class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time Complexity: O(N)
        def simply_rob(houses):
            n = len(houses)
            
            if n <= 2:
                return max(houses)
            
            houses[2] += houses[0]
            for i in range(3, n):
                houses[i] += max(houses[i-3], houses[i-2])

            return max(houses[-1], houses[-2])
        
        if len(nums) <= 3:
            return max(nums)
        return max(simply_rob(nums[:-1]), simply_rob(nums[1:]))