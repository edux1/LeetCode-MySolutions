class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Time Complexity: O(d)
        # Space Complexity: O(d)
        tested_numbers = []
        while not n in tested_numbers:
            tested_numbers.append(n)
            n = sum([int(digit) ** 2 for digit in str(n)])
            if n == 1:
                return True
        return False