class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        
        def _helper(i, j, k):
            if k == len(word):
                return True
            if i == row or j == col or i < 0 or j < 0 or board[i][j] != word[k] or board[i][j] == '#':
                return False
            board[i][j] = '#'
            right = _helper(i, j+1, k+1)
            down = _helper(i+1, j, k+1)
            left = _helper(i, j-1, k+1)
            up = _helper(i-1, j, k+1)
            board[i][j] = word[k]
            return up or down or left or right
            
        
        for r in range(row):
            for c in range(col):
                    if _helper(r,c,0):
                        return True
        return False