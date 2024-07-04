class MinStack:
    # All O(n) methods

    def __init__(self):
        self.stack = []
        self.min_stack = [] # Keeping track of the minimum value

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val) # Finding minimum value to min_stack
        self.min_stack.append(val) # Adds the minimum value for each push

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop() # Don't forget to pop from the min_stack too

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1] # Minimum will always be the top of the min_stack


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()