class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        pointer = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[pointer] = nums[i]
                pointer += 1
                
        return pointer