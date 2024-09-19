class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        # Time Complexity: O(N*M)
        # Space Complexity: O(N*M)
        m, n = len(mat), len(mat[0])
        i, j = 0, 0
        ans = []

        for _ in range(n * m):
            ans.append(mat[i][j])
            if (i + j) % 2 == 0: # Going up
                if j == n-1:
                    i += 1
                elif i == 0:
                    j += 1
                else:
                    i -= 1
                    j += 1
            else: # Going down
                if i == m - 1:
                    j += 1
                elif j == 0:
                    i += 1
                else:
                    i += 1
                    j -= 1
                
        return ans