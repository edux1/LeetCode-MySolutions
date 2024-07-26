class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Time Complexity: O(2^N)
        def getCombinations(start, sum_value, combination):
            if sum_value == target:
                combinations.append(list(combination))
                return
            
            if sum_value > target:
                return
            
            for i in range(start, len(candidates)):
                candidate = candidates[i]
                combination.append(candidate)
                getCombinations(i, sum_value + candidate, combination)
                combination.pop()
        
        candidates.sort()
        combinations = []
        getCombinations(0, 0, [])
        return combinations