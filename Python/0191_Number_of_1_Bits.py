class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        mask = 1
        for i in range(32):
            if n & mask == 1:
                count += 1
            n >>= 1
        return count