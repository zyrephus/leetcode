class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                popped_index = stack.pop()
                height = heights[popped_index]
                width = i if not stack else (i - stack[-1] - 1)
                res = max(res, height * width)

            stack.append(i)

        while stack:
            popped_index = stack.pop()
            height = heights[popped_index]
            width = len(heights) if not stack else (len(heights) - stack[-1] - 1)
            res = max(res, height * width)

        return res
