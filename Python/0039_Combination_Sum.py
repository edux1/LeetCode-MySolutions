class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Time Complexity: O(2^N)
        def getCombinations(i, sum_value, combination):
            candidate = candidates[i]

            sum_value += candidate
            if sum_value > target:
                return
            
            combination.append(candidate)
            
            if sum_value == target:
                print(combination)
                combinations.append(combination)
                return
            
            for j in range(i, len(candidates)):
                getCombinations(j, sum_value, list(combination))
                

        candidates.sort()
        combinations = []

        for i in range(len(candidates)):
            getCombinations(i, 0, [])

        return combinations