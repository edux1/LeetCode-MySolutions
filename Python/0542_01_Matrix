class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        if mat[0][0] != 0:
            mat[0][0] = sys.maxint

        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    if i > 0 and j > 0:
                        mat[i][j] = min(mat[i-1][j], mat[i][j-1]) + 1
                    if i > 0 and not j > 0:
                        mat[i][j] = mat[i-1][j] + 1
                    if not i > 0 and j > 0:
                        mat[i][j] = mat[i][j-1] + 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if mat[i][j] != 0:
                    if i < m-1 and j < n-1:
                        if i == 0 and j == 0:
                            mat[i][j] = min(mat[i+1][j]+1, mat[i][j+1]+1)
                        else:
                            mat[i][j] = min(mat[i+1][j]+1, mat[i][j+1]+1, mat[i][j])
                    if i < m-1 and not j < n-1:
                        mat[i][j] = min(mat[i+1][j] + 1, mat[i][j])
                    if not i < m-1 and j < n-1:
                        mat[i][j] = min(mat[i][j+1] + 1, mat[i][j])

        return mat