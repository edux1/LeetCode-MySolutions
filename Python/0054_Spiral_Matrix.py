class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # Time Complexity: O(N*M)
        # Space Complexity: O(1)
        m, n = len(matrix), len(matrix[0])
        l, r = 0, n-1
        t, b = 0, m-1

        res = []
        i, j = 0, 0

        while l <= r or t <= b:
            # Moving right
            while j < r and t <= b:
                print(matrix[i][j])
                res.append(matrix[i][j])
                j += 1
            t += 1 

            # Moving down
            while i < b and l <= r:
                print(matrix[i][j])
                res.append(matrix[i][j])
                i += 1
            r -= 1

            # Moving left
            while j > l and t <= b:
                print(matrix[i][j])
                res.append(matrix[i][j])
                j -= 1
            b -= 1

            # Moving up
            while i > t and l <= r:
                print(matrix[i][j])
                res.append(matrix[i][j])
                i -= 1
            l += 1

        res.append(matrix[i][j])
        return res