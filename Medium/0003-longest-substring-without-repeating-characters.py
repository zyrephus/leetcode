class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # O(n) solution

        left = 0
        my_set = set()

        res = 0
        for right in range(len(s)):
            # If current char is already in set, it means there's a duplicate
            while s[right] in my_set:
                my_set.remove(s[left])
                left += 1
            
            my_set.add(s[right])

            res = max(res, right - left + 1)
        
        return res
