class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Time Complexity: O(N*N!)
        n = len(nums)
        nums.sort()

        def permute(permutations, permutation, nums):
            n = len(nums)
            if n == 0:
                permutations.append(permutation)
                return
            
            for i in range(n):
                new_list = list(permutation)
                new_list.append(nums[i])
                reduced_list = list(nums)
                reduced_list.pop(i)
                if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                    permute(permutations, new_list, reduced_list)

        permutations = []
        for i in range(n):
            reduced_list = list(nums)
            reduced_list.pop(i)
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                permute(permutations, [nums[i]], reduced_list)
        return permutations