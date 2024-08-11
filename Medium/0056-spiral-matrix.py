class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # O(n * m) solution
        
        total_len = len(matrix) * len(matrix[0])
        res = []
        R, D, L, U = len(matrix[0]), len(matrix), -1, -1 # "Wall" approach
        i, j = 0, 0
        direction = "R"
        
        while len(res) < total_len:
            if direction == "R":
                while j < R:
                    res.append(matrix[i][j])
                    j += 1
                i, j = i + 1, j - 1
                U += 1
                direction = "D"
            elif direction == "D":
                while i < D:
                    res.append(matrix[i][j])
                    i += 1
                i, j = i - 1, j - 1
                R -= 1
                direction = "L"
            elif direction == "L":
                while j > L:
                    res.append(matrix[i][j])
                    j -= 1
                i, j = i - 1, j + 1
                D -= 1
                direction = "U"
            elif direction == "U":
                while i > U:
                    res.append(matrix[i][j])
                    i -= 1
                i, j = i + 1, j + 1
                L += 1
                direction = "R"
            print(res)

        return res