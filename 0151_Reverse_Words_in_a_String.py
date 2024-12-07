class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Time complexity: O(N)
        # Space complexity: O(N)
        words = s.split()
        return " ".join(reversed(words))