class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # O(n + m) solution

        # Count occurrences of each element in nums1
        counter = {}
        for n in nums1:
            counter[n] = 1 + counter.get(n, 0)
        
        res = []
        # Finding common elements in nums2
        for n in nums2:
            if n in counter and counter[n] != 0:
                counter[n] -= 1
                res.append(n)
        
        return res