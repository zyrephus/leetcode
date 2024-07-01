class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # O(n) solution

        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            # Keep popping off the stack until we find a lesser temperature
            while stack and stack[-1][0] < temp:
                stack_t, stack_i = stack.pop() # Tuple unpacking
                res[stack_i] = i - stack_i

            stack.append((temp, i))

        return res