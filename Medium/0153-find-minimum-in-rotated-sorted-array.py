class Solution:
    def findMin(self, nums: List[int]) -> int:
        # O(log n) solution

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else: 
                right = mid # Minimum could be nums[mid]
        
        # left == right
        return nums[left]