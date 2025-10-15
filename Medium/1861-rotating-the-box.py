class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        res = [['.' for i in range(m)] for j in range(n)]

        # Rotate 90 degrees
        for i in range(m):
            for j in range(n):
                res[j][m - 1 - i] = boxGrid[i][j]

        for col in range(m):
            write = n - 1
            for row in range(n - 1, -1, -1):
                if res[row][col] == "*":
                    write = row - 1
                elif res[row][col] == "#":
                    if row != write:
                        res[row][col] = "."
                        res[write][col] = '#'
                    write -= 1

        return res
