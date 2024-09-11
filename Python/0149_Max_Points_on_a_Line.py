class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # Time Complexity: O(N^2)
        # Space Complexity: O(N)
        def findSlope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            if x1-x2 == 0:
                return float('inf')
            return float(y2-y1) / (x2-x1)

        cnt = 1
        for i, p1 in enumerate(points):
            slopes = {}
            for p2 in points[i+1:]:
                slope = findSlope(p1, p2)
                if slope in slopes:
                    slopes[slope] += 1
                else:
                    slopes[slope] = 2
                cnt = max(cnt, slopes[slope])

        return cnt