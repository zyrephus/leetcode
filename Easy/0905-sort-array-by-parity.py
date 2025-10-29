class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = 0, n - 1

        while left < right:
            if not nums[left] % 2:
                left += 1
            elif nums[right] % 2:
                right -= 1
            else: # nums[left] is odd and nums[right] is even
                nums[left], nums[right] = nums[right], nums[left]
                left += 1; right -= 1

        return nums
