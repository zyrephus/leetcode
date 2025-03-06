class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()

        l = 0

        res = 0

        for r in range(len(s)):
            curr = s[r]

            while curr in chars:
                chars.remove(s[l])
                l += 1
            
            chars.add(curr)
            
            res = max(res, r - l + 1)
            
        return res
