class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3: return False

        digits = '0123456789'
        vowels = 'aeiouAEIOU'
        consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

        allowed = digits + vowels + consonants

        has_vowel = False
        has_consonant = False

        for char in word: 
            if char in vowels: has_vowel = True
            if char in consonants: has_consonant = True
            if char not in allowed: return False
        
        return has_vowel and has_consonant