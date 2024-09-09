class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n) solution

        nums_set = set(nums)
        
        res = 0
        for num in nums:
            # Start of a new sequence
            if num - 1 not in nums_set: # O(1) lookup
                curr_res = 1
                i = 1
                while num + i in nums_set:
                    curr_res += 1
                    i += 1
                res = max(res, curr_res)

        return res