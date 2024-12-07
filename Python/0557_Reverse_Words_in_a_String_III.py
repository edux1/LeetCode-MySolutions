class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Time complexity: O(N)
        # Space complexity: O(N)
        s = map(lambda x: x[::-1], s.split())
        return " ".join(s)