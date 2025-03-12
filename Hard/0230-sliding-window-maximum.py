class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        de = deque() # Store indices

        for r in range(len(nums)):
            if de and de[0] < r - k + 1:
                de.popleft()

            while de and nums[de[-1]] < nums[r]:
                de.pop()
            de.append(r)
            
            # Only start adding results when we have processed first k elements
            if r >= k - 1:
                res.append(nums[de[0]])
            
        return res
