class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(s - 1, -1, -1):
            for w in wordDict:
                lenW = len(w)
                if (i + lenW) <= n and s[i : i + lenW] == w:
                    dp[i] = dp[i + lenW]
                if dp[i]:
                    break

        return dp[0]
        
