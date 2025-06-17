class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        digit_to_letter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        def backtrack(i, path):
            if len(path) == len(digits):
                res.append(path)
                return
            
            for char in digit_to_letter[digits[i]]:
                backtrack(i + 1, path + char)

        backtrack(0, "")

        return res
        
