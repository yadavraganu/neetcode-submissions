class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        row = len(matrix)
        col = len(matrix[0])
        matrix.reverse()
        for r in range(row):
            for c in range(r+1,col):
                matrix[r][c],matrix[c][r] = matrix[c][r],matrix[r][c]
            