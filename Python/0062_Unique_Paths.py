class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Time Complexity: O(N*M)
        # Space Complexity: O(N)
        paths = [1] * n
        
        for i in range(1, m):
            for j in range(1, n):
                paths[j] += paths[j-1]

        return paths[-1]