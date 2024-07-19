class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # O(n) solutoin

        res = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                res += 1
            elif res and s[i] == ' ':
                break
        
        return res