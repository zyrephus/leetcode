class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # O(1) solution

        # Rows
        for i in range(9):
            row_set = set()
            for j in range(9):
                n = board[i][j]
                if n in row_set:
                    return False
                elif n != ".":
                    row_set.add(n)

        # Columns
        for i in range(9):
            col_set = set()
            for j in range(9):
                n = board[j][i]
                if n in col_set:
                    return False
                elif n != ".":
                    col_set.add(n)

        # Sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_set = set()
                for k in range(3):
                    for l in range(3):
                        n = board[i + k][j + l]
                        if n in sub_set:
                            return False
                        elif n != ".":
                            sub_set.add(n)
        
        return True