class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        def dfs(i, visited):
            visited.add(i)
            for j in range(n):
                if isConnected[i][j] == 1 and j not in visited:
                    dfs(j, visited)
        
        n = len(isConnected)
        visited = set()
        count = 0

        for i in range(n):
            if i not in visited:
                dfs(i, visited)
                count += 1
        return count