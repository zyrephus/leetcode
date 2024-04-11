class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sortedNums = sorted(nums)
        for i in range(len(sortedNums) - 1):
            if sortedNums[i] == sortedNums[i + 1]:
                return True
        return False