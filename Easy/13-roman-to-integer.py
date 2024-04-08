class Solution:
    def romanToInt(self, s: str) -> int:
        lookup = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500, 
            'M': 1000
        }

        res = 0
        for i in range(len(s)):
            if i != len(s) - 1 and lookup[s[i]] < lookup[s[i + 1]]:
                res -= lookup[s[i]]
            else:
                res += lookup[s[i]]
        return res