class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = []
        subset = []

        def dfs(depth):
            if depth >= len(nums):
                sorted_subset = list(subset)
                sorted_subset.sort()
                if not sorted_subset in subsets:
                    subsets.append(sorted_subset)
                return
            
            subset.append(nums[depth])
            dfs(depth+1)

            subset.pop()
            dfs(depth+1)
        
        dfs(0)
        return subsets