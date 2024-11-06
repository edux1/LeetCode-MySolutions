class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Time Complexity: O(N)
        # Space Complexity: O(1)
        l, r = 0, len(numbers)-1
        while l < r:
            if numbers[r] + numbers[l] > target:
                r -= 1
            elif numbers[r] + numbers[l] < target:
                l += 1
            else:
                return l+1, r+1
            