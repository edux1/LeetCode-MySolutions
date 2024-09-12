class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Time Complexity: O(N)
        # Space Complexity: O(N)
        n = len(nums)
        l, r = 0, n-1
        sorted_squares = [0] * n
        i = n-1
        
        while l < r:
            if abs(nums[l]) >= abs(nums[r]):
                sorted_squares[i] = nums[l]**2
                l += 1
            else:
                sorted_squares[i] = nums[r]**2
                r -= 1
            i -= 1
        
        if l == r:
            sorted_squares[0] = nums[l]**2
        
        return sorted_squares
            