class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        # Time Complexity: O(N)
        # Space Complexity: O(1)
        zeros_to_duplicate = 0
        n = len(arr)
        
        for i in range(n):
            if arr[i] == 0:
                if i + zeros_to_duplicate + 1  == n:
                    arr[-1] = 0
                    n -= 1
                    break
                zeros_to_duplicate += 1
            if i + zeros_to_duplicate + 1 >= n:
                break

        for i in range(n-zeros_to_duplicate-1, -1, -1):
            if arr[i] == 0:
                arr[i + zeros_to_duplicate] = arr[i]
                zeros_to_duplicate -= 1
                if zeros_to_duplicate == 0:
                    break
            arr[i + zeros_to_duplicate] = arr[i]