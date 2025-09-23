class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {} # number: frequency
        max_freq = 0
        count_max = 0

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            
            f = freq[num]

            if f > max_freq:
                max_freq = f
                count_max = 1
            elif f == max_freq:
                count_max += 1
        
        return max_freq * count_max
