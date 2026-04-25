class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        row_map = defaultdict(set)
        col_map = defaultdict(set)
        mini_map = defaultdict(set)

        for r in range(0,9):
            for c in range(0,9):
                if board[r][c] != '.' and board[r][c] in row_map[r]:
                    return False
                else:
                     row_map[r].add(board[r][c])
                
                if board[r][c] != '.' and board[r][c] in col_map[c]:
                    return False
                else:
                     col_map[c].add(board[r][c])

                mini_map_idx = (r//3)*3+(c//3)
                
                if board[r][c] != '.' and board[r][c] in mini_map[mini_map_idx]:
                    return False
                else:
                     mini_map[mini_map_idx].add(board[r][c])
        return True