class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr, used):
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for i in range(len(nums)):
                if used[i] == False:
                    curr.append(nums[i])
                    used[i] = True
                    backtrack(curr, used)
                    curr.pop()
                    used[i] = False

        backtrack([], [False] * len(nums))

        return res
        
