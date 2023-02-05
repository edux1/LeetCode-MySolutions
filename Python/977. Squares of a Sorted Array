class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l, r = 0, len(nums) -1
        list = []
        while l <= r:
            if abs(nums[l]) <= abs(nums[r]):
                list.insert(0,nums[r] ** 2)   
                r -= 1
            else:
                list.insert(0,nums[l] ** 2 ) 
                l += 1
        return list