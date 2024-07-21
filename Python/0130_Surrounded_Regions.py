class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # Complexity time: O(Rows*Cols)
        rows, cols = len(board), len(board[0])

        if rows == 1 or cols == 1:
            return board

        non_surronded_regions = []

        for i in range(1, rows-1):
            for j in range(1, cols-1):
                if board[i][j] != "X":
                    region = self.get_non_surrounded_regions(board, i, j)
                    if region:
                        non_surronded_regions.append(region)
        
        for region in non_surronded_regions:
            for cell in region:
                board[cell[0]][cell[1]] = "O"

    def get_non_surrounded_regions(self, board, i, j):
        # Complexity time: O(Rows*Cols)
        rows, cols = len(board), len(board[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        in_bound = lambda cell: True if 0 <= cell[0] < rows and 0 <= cell[1] < cols else False

        queue = [(i,j)]
        board[i][j] = "X"
        non_surrounded_region = [(i, j)]
        non_surrounded = False
        
        while len(queue) > 0:
            cell = queue.pop(0)

            for direction in directions:
                row = cell[0] + direction[0]
                col = cell[1] + direction[1]
                if in_bound((row, col)) and board[row][col] == "O":
                    queue.append((row, col))
                    board[row][col] = "X"
                    non_surrounded_region.append((row, col))
                    if row == 0 or row == rows-1 or col == 0 or col == cols-1:
                        non_surrounded = True
        
        if non_surrounded:
            return non_surrounded_region
        return None