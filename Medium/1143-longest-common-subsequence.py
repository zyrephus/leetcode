class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        row = [0 for i in range(n + 1)]

        for i in range(m - 1, -1, -1):
            newRow = [0 for i in range(n + 1)]
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    newRow[j] = 1 + row[j + 1]
                else:
                    newRow[j] = max(newRow[j + 1], row[j])
            row = newRow

        return row[0]
        
