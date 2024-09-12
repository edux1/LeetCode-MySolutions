class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Time Complexity: O(M)
        # Space Complexity: O(1)
        h = {}
        for c in magazine:
            if c in h:
                h[c] += 1
            else:
                h[c] = 1
        
        for c in ransomNote:
            if c in h and h[c] > 0:
                h[c] -= 1
            else:
                return False
        
        return True