class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        sol = []

        def backtrack(combination, remain):
            if len(remain) == 0:
                sol.append(list(combination))

            else:
                for i in range(len(remain)):
                    combination.append(remain[i])
                    array = list(remain)
                    array.pop(i)
                    backtrack(combination, array)
                    combination.pop()


        backtrack([], nums)
        return sol 