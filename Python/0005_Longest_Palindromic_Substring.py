class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Time Complexity: O(N^2)
        # Space Complexity: O(N)
        def findPalindrome(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        if len(s) == 1:
            return s
        
        palindrome = ""
        for i in range(len(s)-1):
            new_palindrome1, new_palindrome2 = findPalindrome(i-1, i+1), findPalindrome(i, i+1)
            if len(new_palindrome1) > len(palindrome):
                palindrome = new_palindrome1
            if len(new_palindrome2) > len(palindrome):
                palindrome = new_palindrome2
        return palindrome