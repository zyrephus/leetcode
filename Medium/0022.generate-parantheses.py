class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, string = [], []

        def backtrack(opn, cls):
            if len(string) == 2 * n:
                res.append("".join(string))
                return
            
            if opn < n:
                string.append("(")
                backtrack(opn + 1, cls)
                string.pop()
            
            if opn > cls:
                string.append(")")
                backtrack(opn, cls + 1)
                string.pop()
        
        backtrack(0, 0)
        
        return res
