class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(n^2) solution

        res = []
        n = len(nums)

        nums.sort() # Sort the list

        for i in range(n):
            if nums[i] > 0:
                break
            # We don't want to consider the same number
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            left, right = i + 1, n - 1
            while left < right:
                summ = nums[i] + nums[left] + nums[right]

                if summ == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    left, right = left + 1, right - 1
                    # Skip duplicates for left and right pointers
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1
                elif summ < 0:
                    left += 1
                else:
                    right -= 1
        
        return res