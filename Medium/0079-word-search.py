class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def backtrack(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != word[i]:
                return False

            temp = board[r][c]
            board[r][c] = '#'

            i += 1
            if backtrack(r - 1, c, i) or backtrack(r + 1, c, i) or backtrack(r, c + 1, i) or backtrack(r, c - 1, i):
                return True

            board[r][c] = temp

        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True

        return False
        
