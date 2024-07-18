class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # O(log n) solution

        left, right = 0, len(nums) - 1

         # Binary search
        while left <= right:
            m = (left + right) // 2 # Integer division by two
            if target < nums[m]:
                right = m - 1
            elif target > nums[m]:
                left = m + 1
            else:
                return m
        
        return left
            