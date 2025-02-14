class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        bucket = [[] for i in range(len(nums) + 1)]
        for num, frequency in freq.items():
            bucket[frequency].append(num)
        
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)

                if len(res) == k: 
                    return res
