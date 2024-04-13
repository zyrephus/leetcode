class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxVal, cur = 0, 0
        
        for n in nums:
            if n == 1:
                cur += 1
                print(cur)
            else:
                maxVal = max(maxVal, cur)
                cur = 0
        maxVal = max(maxVal, cur)

        return maxVal