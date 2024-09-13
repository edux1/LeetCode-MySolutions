class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # Time Complexity: O(N)
        # Space Complexity: O(N)
        h = set()

        for n in arr:
            if n * 2 in h or (n % 2 == 0 and n / 2 in h):
                return True
            h.add(n)
        return False
