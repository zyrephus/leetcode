class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        p_hash = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
    
        for p in s:
            if p in p_hash and stack and p_hash[p] == stack[-1]:
                stack.pop()
            else:
                stack.append(p)

        return not bool(stack)
