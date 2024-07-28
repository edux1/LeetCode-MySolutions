class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def getCombinations(left, right, combination):
            if left == right == n:
                combinations.append(combination)
                return
            
            if left < n:
                getCombinations(left+1, right, combination + "(")

            if right < left:
                getCombinations(left, right+1, combination + ")")        

        combinations = []
        getCombinations(0, 0, "")
        return combinations