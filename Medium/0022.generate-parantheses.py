class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # I have no idea what the time complexity is and am too lazy to check

        stack = []
        res = []

        def backtrack(open_n, closed_n):
            if open_n == closed_n == n:
                res.append(''.join(stack)) # Join all () as one element
            if open_n < n: # Add ( if open < n
                stack.append('(')
                backtrack(open_n + 1, closed_n)
                stack.pop()
            if closed_n < open_n:         # Add ) if closed < open
                stack.append(')')
                backtrack(open_n, closed_n + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res