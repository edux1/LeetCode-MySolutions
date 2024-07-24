class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Time complexity: O(N*(2^N))
        subsets = []
        subset = []

        def dfs(depth):
            if depth >= len(nums):
                subsets.append(list(subset))
                return
            
            subset.append(nums[depth])
            dfs(depth+1)

            subset.pop()
            dfs(depth+1)

        dfs(0)
        return subsets