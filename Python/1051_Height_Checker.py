class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # Time Complexity: O(N log(N))
        # Space Complexity: O(N)
        expected = heights[:]
        expected.sort()
        cnt = 0

        for i in range(len(heights)):
            if expected[i] != heights[i]:
                cnt += 1

        return cnt