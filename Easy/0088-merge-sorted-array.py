class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        p1, p2, pMax = m - 1, n - 1, m + n - 1
        
        # Starting from the largest element and moving in decreasing order
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[pMax] = nums1[p1]
                p1 -= 1
            else:
                nums1[pMax] = nums2[p2]
                p2 -= 1
            pMax -= 1
        
        # Fills nums1 with leftover nums2 elements (guaranteed smaller)
        while p2 >= 0:
            nums1[pMax] = nums2[p2]
            p2 -= 1
            pMax -= 1
      
