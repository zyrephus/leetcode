class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(n) solution

        # Getting frequency of each color
        counts = [0, 0, 0]
        for color in nums:
            counts[color] += 1
        
        r, w, b = counts # Unpacking
        nums[:r]     = [0] * r # Start from 0 to r
        nums[r:w]    = [1] * w # Start from r to w
        nums[r + w:] = [2] * b # Start from r + w to end