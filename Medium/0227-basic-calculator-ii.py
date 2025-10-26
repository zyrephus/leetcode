class Solution:
    def calculate(self, s: str) -> int:
        i, n = 0, len(s)
        stack = []
        op = "+"
        curr_num = 0

        while i < n:
            char = s[i]

            if char.isdigit():
                curr_num = curr_num * 10 + (ord(char) - 48)

            if char in "+-*/" or i == n - 1:
                if op == "+":
                    stack.append(curr_num)
                elif op == "-":
                    stack.append(-curr_num)
                elif op == "*":
                    stack.append(stack.pop() * curr_num)
                else: # "/":
                    stack.append(int(stack.pop() / curr_num))
                
                op = char
                curr_num = 0
            
            i += 1

        return sum(stack)
        
