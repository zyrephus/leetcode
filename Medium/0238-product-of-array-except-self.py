class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [1], [1]

        cur = 1
        for i in range(len(nums) - 1):
            cur *= nums[i]
            left.append(cur)
        cur = 1
        for i in range(len(nums) - 1, 0, -1):
            cur *= nums[i]
            right.append(cur)
        
        res = []
        for i in range(len(nums)):
            j = -i - 1
            res.append(left[i] * right[j])

        return res
