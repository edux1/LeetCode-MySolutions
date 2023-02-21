class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        fresh, rotten = set(), []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                elif grid[i][j] == 2:
                    rotten.append((i,j))
        
        time = 0

        while fresh and rotten:
            newrotten = []
            for i, j in rotten:
                for coord in ((i-1,j), (i+1,j), (i,j-1), (i,j+1)):
                    if coord in fresh:
                        fresh.remove(coord)
                        newrotten.append(coord)
            rotten = newrotten
            time += 1

        return -1 if fresh else time