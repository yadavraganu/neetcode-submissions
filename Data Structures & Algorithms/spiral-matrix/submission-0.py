from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0]) - 1
        top, down = 0, len(matrix) - 1
        res = []

        while left <= right and top <= down:
            # Traverse from left to right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            # Traverse from top to bottom
            for i in range(top, down + 1):
                res.append(matrix[i][right])
            right -= 1

            # Traverse from right to left
            if top <= down:
                for i in range(right, left - 1, -1):
                    res.append(matrix[down][i])
                down -= 1

            # Traverse from bottom to top
            if left <= right:
                for i in range(down, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res
