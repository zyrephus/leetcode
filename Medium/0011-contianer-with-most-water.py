class Solution:
    def maxArea(self, height: List[int]) -> int:
        # O(n) solution
        
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            length = min(height[left], height[right])
            curr_area = length * width
            max_area = max(max_area, curr_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area