class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # O(n) solution

        # Getting the frequencies in a dicitonary
        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        
        # Calculating the result as the length of the list minus the frequency of val
        res = len(nums) - freq.get(val, 0)
        index = 0
        for n in freq:
            if n == val: # Skips val
                continue
            for i in range(freq[n]):
                nums[index] = n
                index += 1
    
        return res