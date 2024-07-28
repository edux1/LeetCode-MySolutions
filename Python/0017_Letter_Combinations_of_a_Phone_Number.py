class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # Time Complexity: O(3^N)
        combinations = []
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def getCombinations(pos, combination):
            if pos >= len(digits):
                if combination != "":
                    combinations.append(combination)
                return
            
            key = digits[pos]
            key_letters = letters[digits[pos]]
            for letter in key_letters:
                combination += letter
                getCombinations(pos+1, combination)
                combination = combination[:-1]
            
        
        getCombinations(0, "")
        return combinations