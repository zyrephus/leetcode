class Solution:
    def isValid(self, s: str) -> bool:
        # O(n) solution

        dic = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        res = []

        for i in range(len(s)):
            if s[i] in "([{":
                res.append(s[i])
            else:
                if not res or res[-1] != dic[s[i]]:
                    return False
                res.pop()

        return not res