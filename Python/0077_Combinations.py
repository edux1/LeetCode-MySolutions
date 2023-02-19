class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        sol = []

        def backtrack(remain, combination, num):
            if remain == 0:
                sol.append(list(combination))
            
            else:
                for i in range(num, n+1):
                    combination.append(i)
                    backtrack(remain-1, combination, i+1)
                    combination.pop()


        backtrack(k, [], 1)
        return sol