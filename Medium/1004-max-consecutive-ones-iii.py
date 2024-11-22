class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # O(n) solution

        res = 0
        num_zeros = 0
        
        l = 0

        for r in range(len(nums)):
            # Flipping if we encounter 0
            if nums[r] == 0:
                num_zeros += 1
            
            # Restricting window if # of 0s > k
            while num_zeros > k:
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1
            
            # Calculating window length
            curr_len = r - l + 1
            res = max(res, curr_len)
        
        return res
        