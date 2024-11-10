class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # O(log n) solution

        low, mid, high = 0, 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2 # Integer division

            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
            
        return -1