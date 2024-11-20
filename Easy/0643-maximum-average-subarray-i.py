class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # O(n) solution

        # Initializing the first window
        curr_sum = sum(nums[:k])  # Sum of the first 'k' elements
        max_sum = curr_sum  # Track the maximum sum found so far

        # Sliding window across nums
        for i in range(k, len(nums)):
            curr_sum = curr_sum - nums[i - k] + nums[i]  # Slide the window
            max_sum = max(max_sum, curr_sum)  # Update maximum if necessary

        return max_sum / k  # Return the maximum average
