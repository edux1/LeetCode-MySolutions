class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # Time Complexity: O(N)
        # Space Complexity: O(1)
        n = len(s)
        l, r = 0, n-1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1