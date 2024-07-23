class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        lenS = len(s)
        res = ""
        for r in range(numRows):
            jump = (numRows - 1) * 2
            for i in range(r, lenS, jump):
                res += s[i]
                midJump = i + jump - 2 * r
                if r != 0 and r != numRows - 1 and midJump < lenS:
                    res += s[midJump]
        
        return res