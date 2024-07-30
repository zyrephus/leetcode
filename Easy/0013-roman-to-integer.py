class Solution:
    def romanToInt(self, s: str) -> int:
        # O(n) solution

        # Map of Roman numerals to their integer values
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        
        res = 0

        # Iterate through the string from right to left
        for i in range(len(s) - 1, -1, -1):
            curr = symbols[s[i]]
            
            # If the current value is less than the next value, subtract it
            if i + 1 < len(s) and curr < symbols[s[i + 1]]:
                curr = -curr

            res += curr

        return res