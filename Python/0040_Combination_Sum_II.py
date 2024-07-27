class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Time Complexity: O(2^N)
        def getCombinations(start, target, combination):
            if target == 0:
                combinations.append(list(combination))
                return
            
            if target < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                combination.append(candidates[i])
                getCombinations(i+1, target - candidates[i], combination)
                combination.pop()

        combinations = []
        candidates.sort()
        getCombinations(0, target, [])
        return combinations

        