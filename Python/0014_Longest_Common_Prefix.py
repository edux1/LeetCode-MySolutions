class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Time Complexity: O(N*M)
        # Space Complexity: O(N)
        exit = False
        
        i = 0
        while i < len(strs[0]):
            char = strs[0][i]

            for word in strs[1:]:
                if i >= len(word) or char != word[i]:
                    return word[:i]
            i += 1
        return strs[0][:i]