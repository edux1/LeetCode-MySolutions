class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # Time complexity: O(N^2)
        # Space complexity: O(N)
        row = [1]

        for _ in range(rowIndex):
            row = [1] + [row[j] + row[j+1] for j in range(len(row)-1)] + [1]

        return row