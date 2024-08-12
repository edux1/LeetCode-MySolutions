class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time Complexity: O(N)
        n = len(nums)
        if n == 1:
            return 0
        fuel1, fuel2 = nums[0]-1, 0
        count = 1

        for i in range(1, n):
            if(nums[i] > fuel2):
                fuel2 = nums[i]
            if fuel1 == 0 and i < n-1:
                fuel1 = fuel2
                fuel2 = 0
                count += 1
            fuel1 -= 1
            fuel2 -= 1
        
        return count