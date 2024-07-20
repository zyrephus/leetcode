class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # O(n) solution

        for i in range(len(digits) - 1, -1, -1): # Traversing digits in reverse order
            if digits[i] < 9: # Just add one and return 
                digits[i] += 1
                return digits
            digits[i] = 0 # If the digit is equal to 9
        
        return [1] + digits 