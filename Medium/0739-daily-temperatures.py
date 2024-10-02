class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # O(n) soltuion

        res = [0] * len(temperatures)
        stack = []

        for i, temperature in enumerate(temperatures):
            # Keep popping off stack until we arrive at a temperature (in the stack) > current temperature
            while stack and temperature > stack[-1][0]:
                stack_t, stack_i = stack.pop()
                res[stack_i] = i - stack_i

            stack.append((temperature, i))
        
        return res