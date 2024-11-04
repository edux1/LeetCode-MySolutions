class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Time Complexity: O(N+M)
        # Space Complexity: O(N)
        m, n = len(haystack), len(needle)
        
        lps = [0] * n

        i, j = 1, 0
        while i < n:
            if needle[i] == needle[j]:
                j += 1
                lps[i] = j
                i += 1
            elif j != 0:
                j = lps[j-1]
            else:
                i += 1

        i, j = 0, 0
        while i < m:
            if haystack[i] == needle[j]:
                j += 1
                i += 1
                if j == n:
                    return i - j
            elif j != 0:
                j = lps[j-1]
            else:
                i += 1
        return -1