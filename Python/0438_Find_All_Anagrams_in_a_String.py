class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []

        anagram, h = {}, {}
        res = []
        for c in p:
            if c in anagram:
                anagram[c] += 1
            else:
                anagram[c] = 1
                h[c] = 0
        
        for i in range(len(p)):
            if s[i] in h:
                h[s[i]] += 1
                if h == anagram:
                    res.append(i-len(p)+1)
            
        for i in range(len(p), len(s)):
            if s[i] in h:
                h[s[i]] += 1   
            if s[i-len(p)] in h:
                h[s[i-len(p)]] -= 1
            if h == anagram:
                res.append(i-len(p)+1)
        
        return res