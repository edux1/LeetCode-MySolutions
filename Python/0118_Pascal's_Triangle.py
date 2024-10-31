class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # Time Complexity: O(N^2)
        # Space Complexity: O(N^2)
        res = []

        for i in range(numRows):
            arr = []
            
            for j in range(i+1):
                if j == 0 or j == i:
                    arr.append(1)
                else:
                    arr.append(res[i-1][j-1] + res[i-1][j])
            
            res.append(arr)
        return res