class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        sol = []

        def backtrack(start, str):
            if start == len(str):
                sol.append(str)

            else:
                backtrack(start+1, str[:start]+str[start:].lower())
                if str[start].isalpha():
                    backtrack(start+1, str[:start]+str[start:].capitalize())
        
        backtrack(0, s)
        return sol