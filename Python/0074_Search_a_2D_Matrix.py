class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        top, bottom = 0, len(matrix)-1
        l, r = 0, len(matrix[0])-1

        while top < bottom:
            mid = (top+bottom)/2
            if matrix[mid][0] > target:
                bottom = mid - 1
            elif matrix[mid][r] >= target:
                top = bottom = mid
            else:
                top = mid + 1

        while l < r:
            mid = (l+r)/2
            if matrix[top][mid] == target:
                return True
            elif matrix[top][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        if matrix[top][l] == target:
            return True
        return False