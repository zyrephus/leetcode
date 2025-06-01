class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return

            # Don't pick next number
            backtrack(i + 1)

            # Pick next number
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()

        backtrack(0)

        return res
        
