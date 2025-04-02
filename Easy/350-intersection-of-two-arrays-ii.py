class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_1 = {}
        for num in nums1:
            hash_1[num] = 1 + hash_1.get(num, 0)
        
        res = []
        for num in nums2:
            if num in hash_1 and hash_1[num] > 0:
                res.append(num)
                hash_1[num] -= 1

        return res
        
