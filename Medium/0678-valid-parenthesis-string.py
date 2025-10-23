class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []
        for i, char in enumerate(s):
            if char == "(":
                left.append(i)
            elif char == "*":
                star.append(i)
            else:
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False

        # Match remaining "(" with later '*'
        while left and star:
            if left[-1] > star[-1]:
                return False
            left.pop()
            star.pop()

        return not left
