class Solution:
    def trap(self, height: List[int]) -> int:
        # O(n) solution

        left = right = 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n

        for i in range(n):
            j = -i - 1
            max_left[i] = left
            max_right[j] = right
            left = max(left, height[i])
            right = max(right, height[j])
        
        res = 0
        for i in range(n):
            potential_water = min(max_left[i], max_right[i])
            res += max(0, potential_water - height[i])
        
        return res