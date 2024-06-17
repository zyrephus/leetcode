class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # O(n + m) solution

        counter = {}
        for char in ransomNote:
            counter[char] = 1 + counter.get(char, 0)
        
        for char in magazine:
            if char in counter:
                counter[char] -= 1
                if counter[char] == 0:
                    del counter[char]
        
        return not counter