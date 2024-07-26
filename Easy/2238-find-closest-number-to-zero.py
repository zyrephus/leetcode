class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # O(n) solution
        
        closest = nums[0]
        for i in range(1, len(nums)):
            if abs(nums[i]) < abs(closest):
                closest = nums[i]
            elif abs(nums[i]) == abs(closest):
                closest = max(nums[i], closest)
        return closest