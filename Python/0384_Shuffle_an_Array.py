import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        self.original = nums
        

    def reset(self):
        """
        :rtype: List[int]
        """
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        return self.original

    def shuffle(self):
        """
        :rtype: List[int]
        """
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        arr = self.original[:]
        random.shuffle(arr)
        return arr
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()