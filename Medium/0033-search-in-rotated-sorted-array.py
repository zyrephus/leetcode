class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find minimum in array
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        min_pos = left
        
        # Determine which half to search
        if target < nums[0]:
            # left = min_pos
            right = len(nums) - 1
        elif target > nums[0]:
            left = 0
            right = min_pos - 1 if min_pos - 1 > -1 else len(nums) - 1
        else:
            return 0

        # Find target
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        
        return -1
