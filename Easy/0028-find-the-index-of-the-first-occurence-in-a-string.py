class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # O((n − m) * m) solution
        h, n = len(haystack), len(needle)

        for i in range(h - n + 1):
            if haystack[i : i + n] == needle:
                return i

        return -1