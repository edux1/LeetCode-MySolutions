class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # Time Complexity: O(log(N))
        # Space Complexity: O(1)
        count = 0
        while left != right:
            left >>= 1
            right >>= 1
            count += 1
        return left << count