class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        n = len(s)
        
        prev1, prev2 = 1, 1
        for i in range(1, n):            
            curr = 0
            if s[i] != "0":
                curr += prev1
            if 10 <= int(s[i-1:i+1]) <= 26:
                curr += prev2

            prev1, prev2 = curr, prev1

        return prev1
