class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited, queue = [], []

        m = len(grid)
        n = len(grid[0])
        maximum = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    visited.append((i,j))
                    queue.append((i,j))
                    count = 0
                    while len(queue) > 0:
                        x, y = queue.pop(0)
                        count += 1
                        if x > 0 and grid[x-1][y] == 1 and not (x-1,y) in visited:
                            visited.append((x-1,y))
                            queue.append((x-1,y))
                        if y > 0 and grid[x][y-1] == 1 and not (x, y-1) in visited:
                            visited.append((x,y-1))
                            queue.append((x,y-1))
                        if x < m-1 and grid[x+1][y] == 1 and not (x+1, y) in visited:
                            visited.append((x+1,y))
                            queue.append((x+1,y))
                        if y < n-1 and grid[x][y+1] == 1 and not (x, y+1) in visited:
                            visited.append((x,y+1))
                            queue.append((x,y+1))
                    maximum = max(maximum, count)
        return maximum
                        
