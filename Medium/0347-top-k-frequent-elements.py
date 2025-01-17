class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n) solution
        
        nums_map = {} # Frequency of numbers
        
        freq = [[] for i in range(len(nums) + 1)] # Bucket sort

        # Counting frequency
        for i in nums:
            nums_map[i] = 1 + nums_map.get(i, 0)

        # Grouping numbers by their frequency
        for num, count in nums_map.items():
            freq[count].append(num)

        # Traverse frequency list from high to low
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                
                if len(res) == k:
                    return res
