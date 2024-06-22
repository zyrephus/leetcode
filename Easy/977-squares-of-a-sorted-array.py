class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # O(n) solution

        left = 0
        right = len(nums) - 1
        res = []

        # Two-pointer approach for comparing outer numbers
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                res.append(nums[right] ** 2)
                right -= 1
            else:
                res.append(nums[left] ** 2)
                left += 1
        
        res.reverse() # O(n)
        return res
    