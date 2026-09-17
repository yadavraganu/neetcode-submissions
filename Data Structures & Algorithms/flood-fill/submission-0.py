class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row = len(image)
        col = len(image[1])
        k = image[sr][sc]
        def traverse(i,j):
            if i >= row or j >= col or i < 0 or j < 0 or image[i][j] != k:
                return
            image[i][j] = 'X'
            traverse(i+1,j)
            traverse(i-1,j)
            traverse(i,j+1)
            traverse(i,j-1)
        traverse(sr,sc)
        for r in range(row):
            for c in range(col):
                if image[r][c] == 'X':
                    image[r][c] = color
        return image