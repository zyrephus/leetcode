class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # O(m + n) solution

        freq = {}

        # Getting the frequency of characters in magazine
        for c in magazine:
            freq[c] = 1 + freq.get(c, 0)
        
        # Check if each character in ransomNote can be constructed
        for c in ransomNote:
            if freq.get(c, 0) > 0:
                freq[c] -= 1
            else:
                return False
        
        return True