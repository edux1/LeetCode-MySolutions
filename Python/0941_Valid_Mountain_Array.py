class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # Time Complexity: O(N)
        # Space Complexity: O(1)
        n = len(arr)
        if n < 3:
            return False

        i = 0

        while i+1 < n and arr[i] < arr[i+1]:
            i += 1
        
        if i == 0 or i == n-1:
            return False

        while i+1 < n and arr[i] > arr[i+1]:
            i += 1
        
        return i == n-1
        
