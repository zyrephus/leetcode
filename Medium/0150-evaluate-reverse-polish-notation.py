class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # O(n) solution

        stack = [] # Using stack approach

        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                # Need to store in variable since the order matters
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                # Same as subtraction
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a)) # Will round towards 0
            else:
                stack.append(int(c)) # Add to stack if it's not an operator
        
        return stack[0]