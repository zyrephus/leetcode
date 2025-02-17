class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set) # key = (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                curr = board[r][c]

                if curr == ".":
                    continue

                if (curr in rows[r] or 
                curr in cols[c] or 
                curr in squares[(r // 3, c // 3)]):
                    return False
                
                rows[r].add(curr)
                cols[c].add(curr)
                squares[(r // 3, c // 3)].add(curr)
            
        return True
