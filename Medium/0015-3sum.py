class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            
            # Skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])

                    r -= 1
                    l += 1

                    # Skip duplicate values for l
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        return res
