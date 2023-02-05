class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        
        visited, queue = [], []

        visited.append((sr,sc))
        queue.append((sr,sc))
        
        num = image[sr][sc]
        m = len(image)
        n = len(image[0])

        while len(queue) > 0:
            i, j = queue.pop(0)
            image[i][j] = color
            if i > 0 and image[i-1][j] == num and not (i-1, j) in visited:
                visited.append((i-1,j))
                queue.append((i-1,j))
            if j > 0 and image[i][j-1] == num and not (i, j-1) in visited:
                visited.append((i,j-1))
                queue.append((i, j-1))
            if i < m-1 and image[i+1][j] == num and not (i+1, j) in visited:
                visited.append((i+1,j))
                queue.append((i+1, j))
            if j < n-1 and image[i][j+1] == num and not (i, j+1) in visited:
                visited.append((i,j+1))
                queue.append((i, j+1))
        return image

