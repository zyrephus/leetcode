class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # O(n) solution

        left = 0
        right = len(nums) - 1
        res = []
        
        # Squares of each number in decreasing order
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res.append(nums[left] ** 2)
                left += 1
            else:
                res.append(nums[right] ** 2)
                right -= 1
        
        left = 0
        right = len(nums) - 1

        # Reversing since we need non-decreasing order
        while left <= right:
            temp = res[left]
            res[left] = res[right]
            res[right] = temp
            left += 1
            right -= 1
        
        return res