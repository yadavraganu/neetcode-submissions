class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        result = []
        board = [["."]*n for _ in range(n)] 
        col = set()
        pos_diag = set()
        neg_diag = set()

        def _helper(r):

            if r == n:
                result.append(list("".join(row) for row in board))
                return
            
            for c in range(n):
                
                if c in col or (r+c) in neg_diag or (r-c) in pos_diag:
                    continue
                    
                col.add(c)
                pos_diag.add(r-c)
                neg_diag.add(r+c)

                board[r][c] = 'Q'

                _helper(r+1)

                board[r][c] = '.'

                col.remove(c)
                pos_diag.remove(r-c)
                neg_diag.remove(r+c)

        _helper(0)

        return result
