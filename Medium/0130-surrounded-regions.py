class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def markSafe():
            q = deque()

            # Start from border
            for r in range(ROWS):
                for c in range(COLS):
                    if r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1 and board[r][c] == 'O':
                        q.append((r, c))
            
            while q:
                r, c = q.popleft()

                # Mark the 'safe' O's
                if board[r][c] == 'O':
                    board[r][c] = '#'
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < ROWS and 0 <= nc < COLS:
                            q.append((nr, nc))
        
        markSafe() 

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'
