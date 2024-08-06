class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # Time Complexity: O(N*M*(3^K))
        def wordFound(i, j, index, visited):
            if index >= len(word):
                return True

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            for direction in directions:
                x = i + direction[0]
                y = j + direction[1]

                if 0 <= x < m and 0 <= y < n:
                    if not visited[x][y] and board[x][y] == word[index]:
                        visited[x][y] = True
                        if wordFound(x, y, index + 1, visited):
                            return True
                        visited[x][y] = False
            return False

        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if wordFound(i, j, 1, visited):
                        return True
                    visited[i][j] = False

        return False