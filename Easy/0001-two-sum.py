class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in indices:
                return [indices[diff], i]
            
            indices[nums[i]] = i
