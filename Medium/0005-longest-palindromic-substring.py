class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        bestL, bestR = 0, 1 # [L, R)

        def expand(l, r):
            nonlocal bestL, bestR

            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1; r += 1

            L, R = l + 1, r
            if R - L > bestR - bestL:
                bestL, bestR = L, R

        for i in range(n):
            expand(i, i) # Odd
            expand(i, i + 1) # Even
            
        return s[bestL:bestR]
        
