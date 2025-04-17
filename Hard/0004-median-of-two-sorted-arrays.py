class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        small, large = nums1, nums2

        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums2) < len(nums1):
            small, large = nums2, nums1
        
        left, right = 0, len(small) - 1
        while True:
            i = (left + right) // 2 # small
            j = half - i - 2 # large

            small_left = small[i] if i >= 0 else float("-infinity")
            small_right = small[i + 1] if (i + 1) < len(small) else float("infinity")
            large_left = large[j] if j >= 0 else float("-infinity")
            large_right = large[j + 1] if (j + 1) < len(large) else float("infinity")

            # Correct partition
            if small_left <= large_right and large_left <= small_right:
                # Odd case
                if total % 2:
                    return min(small_right, large_right)
                # Even case
                return (max(small_left, large_left) + min(small_right, large_right)) / 2
            elif small_left > large_right:
                right = i - 1
            else:
                left = i + 1
