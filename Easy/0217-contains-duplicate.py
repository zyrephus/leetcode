class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # O(n) solution

        number_map = {}
        for num in nums:
            if num in number_map:
                return True
            else:
                number_map[num] = 1
        return False