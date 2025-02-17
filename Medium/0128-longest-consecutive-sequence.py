class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                max_seq = 1

                while num + max_seq in nums_set:
                    max_seq += 1
                
                res = max(res, max_seq)
        
        return res
                
