class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n) solution

        max_len = 0
        s = set(nums)

        for n in nums:
            if (n - 1) not in s:
                curr_len = 1
                next_n = n + 1
                while next_n in s:
                    curr_len += 1
                    next_n += 1
                max_len = max(max_len, curr_len)

        return max_len