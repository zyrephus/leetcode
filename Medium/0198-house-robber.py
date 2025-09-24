class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        prev1, prev2 = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            prev1, prev2 = prev2, max(prev2, prev1 + nums[i])

        return prev2
