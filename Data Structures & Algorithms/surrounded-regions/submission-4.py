class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def traverse(l,m):
            if l < 0 or m < 0 or l >= len(board) or m >= len(board[0]) or board[l][m] != 'O':
                return
            board[l][m] = 'T'
            traverse(l,m+1)
            traverse(l,m-1)
            traverse(l+1,m)
            traverse(l-1,m)

        # All border rows
        for i in range(len(board)):
            if board[i][0] == "O":
                traverse(i,0)
            if board[i][len(board[0])-1] == "O":
                traverse(i,len(board[0])-1)
        for i in range(len(board[0])):
            if board[0][i] == "O":
                traverse(0,i)
            if board[len(board)-1][i] == "O":
                traverse(len(board)-1,i)

        for l in range(len(board)):
            for m in range(len(board[0])):
                if board[l][m] == 'O':
                    board[l][m] = 'X'
                elif board[l][m] == 'T':
                    board[l][m] = 'O'

