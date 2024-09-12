class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time Complexity: O(N)
        # Space Complexity: O(1)
        cnt = 0
        for n in nums:
            if len(str(n)) % 2 == 0:
                cnt += 1
        
        return cnt