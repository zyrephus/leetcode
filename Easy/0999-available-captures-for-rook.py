class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        DIRS = ((0, 1), (0, -1), (1, 0), (-1, 0))

        # Find rook position
        rr = rc = -1
        for row in range(8):
            for col in range(8):
                if board[row][col] == "R":
                    rr, rc = row, col
                    break
            if rr != -1:
                break

        res = 0
        for dr, dc in DIRS:
            r, c = rr + dr, rc + dc
            while 0 <= r < 8 and 0 <= c <8:
                if board[r][c] == "B":
                    break
                elif board[r][c] == "p":
                    res += 1
                    break
                    
                r += dr
                c += dc

        return res
