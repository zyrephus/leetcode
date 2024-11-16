class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # O(log n) solution

        # Find minimum in array
        left, right = 0, len(nums) - 1

        while left < right:
            m = (left + right) // 2

            if nums[m] > nums[right]:
                left = m + 1
            else:
                right = m # nums[right] could still be
        
        min_pos = left # Position of minimum number

        if target < nums[0]:
            left = min_pos # Redundant
            right = len(nums) - 1
        elif target > nums[0]:
            left = 0
            right = min_pos - 1 if min_pos - 1 > -1 else len(nums) - 1
        else:
            return 0

        while left <= right:
            m = (left + right) // 2

            if nums[m] > target:
                right = m - 1
            elif nums[m] < target:
                left = m + 1
            else:
                return m

        return -1
