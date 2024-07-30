class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # O(t) solution

        sLen, tLen = len(s), len(t)

        if sLen > tLen: return s == t
        if not s: return True

        j = 0
        # Comparing each character of t to each character of s
        for i in range(tLen):
            if s[j] == t[i]:
                j += 1
                if j == sLen:
                    return True
        
        return False