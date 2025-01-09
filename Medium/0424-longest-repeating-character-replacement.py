class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # O(n) solution  

        count = {} # Hashmap to count occurences of letters

        res = 0
        
        # Sliding window
        left = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0) # Update frequency of letters
            
            # Shift left if number of operations exceed k
            if (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res