class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2) < len(s1):
            return False

        h1 = {}
        h2 = {}
        for i in range(len(s1)):
            if s1[i] in h1:
                h1[s1[i]] += 1
            else:
                h1[s1[i]] = 1
            h2[s1[i]] = 0

        i = 0
        k = len(s1)
        while i < k:
            if s2[i] in h2:
                h2[s2[i]] += 1
            if h2 == h1:
                return True
            i += 1

        while i < len(s2):
            if s2[i] in h2:
                h2[s2[i]] += 1
            if s2[i-k] in h2:
                h2[s2[i-k]] -= 1
            if h2 == h1:
                return True
            i += 1
        return False
