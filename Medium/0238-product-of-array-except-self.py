class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) solution

        l_mult = 1
        r_mult = 1
        n = len(nums)
        left = [None] * n
        right = [None] * n

        for i in range(n):
            j = -i - 1
            left[i] = l_mult
            right[j] = r_mult
            l_mult *= nums[i]
            r_mult *= nums[j]

        return [l * r for l, r in zip(left, right)]
