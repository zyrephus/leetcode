class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # O(n) solution

        res = []
        
        i = 0
        while i < len(nums):
            start = nums[i]
            
            # Continue if numbers increase by 1
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                i += 1
            
            if start != nums[i]:
                res.append(f"{start}->{nums[i]}")
            else:
                res.append(f"{nums[i]}")
            
            i += 1
        
        return res