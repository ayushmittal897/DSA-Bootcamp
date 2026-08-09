class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        m = len(board)
        n = len(board[0])

        def live_neighbors(r, c):
            count = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] in (1, 2):
                        count += 1
            return count

        for i in range(m):
            for j in range(n):
                live = live_neighbors(i, j)
                if board[i][j] == 1 and (live < 2 or live > 3):
                    board[i][j] = 2
                elif board[i][j] == 0 and live == 3:
                    board[i][j] = 3

        for i in range(m):
            for j in range(n):
                board[i][j] %= 2
