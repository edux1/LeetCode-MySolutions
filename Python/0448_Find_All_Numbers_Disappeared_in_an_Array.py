class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Time Complexity: O(N)
        # Space Complexity: O(1)
        for i in range(len(nums)):
            nums[abs(nums[i])-1] = -abs(nums[abs(nums[i])-1])

        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i+1)

        return ans