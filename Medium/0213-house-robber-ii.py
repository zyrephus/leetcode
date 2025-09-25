class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def robLinear(lo: int, hi: int) -> int:
            prev1, prev2 = 0, 0

            for i in range(lo, hi):
                prev1, prev2 = max(prev1, prev2 + nums[i]), prev1

            return prev1

        return max(robLinear(0, n - 1), robLinear(1, n))
