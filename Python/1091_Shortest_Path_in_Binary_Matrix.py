from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        start, end = (0, 0), (n-1, n-1)

        # Helper functions
        in_bound = lambda cell: 0 <= cell[0] < n and 0 <= cell[1] < n

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        blocked = grid

        if start == end:
            return 1 if grid[0][0] == 0 else -1
        
        if grid[0][0] != 0:
            return -1
        
        queue = deque()
        queue.append(((0, 0), 1))

        while len(queue) > 0:
            cell, distance = queue.popleft()
            if cell == end:
                return distance
            blocked[cell[0]][cell[1]] = 1
            for direction in directions:
                fil, col = cell[0] + direction[0], cell[1] + direction[1]
                if in_bound((fil, col)) and not blocked[fil][col]:
                    blocked[fil][col] = 1
                    queue.append(((fil, col), distance + 1))
        return -1
