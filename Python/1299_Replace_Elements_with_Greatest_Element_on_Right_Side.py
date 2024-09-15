class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # Time Complexity: O(N)
        # Space Complexity: O(1)
        greatest = arr[-1] 
        arr[-1] = -1
        for i in range(len(arr)-2, -1, -1):
            tmp = arr[i]
            arr[i] = greatest
            greatest = max(tmp,greatest)
        return arr