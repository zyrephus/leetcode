class Solution:
    def isPalindrome(self, s: str) -> bool:
        # O(n) solution

        alphanumeric = set('abcdefghijklmnopqrstuvwxyz1234567890')

        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left].lower() not in alphanumeric:
                left += 1
                continue
            if s[right].lower() not in alphanumeric:
                right -= 1
                continue

            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
                continue
            else:
                return False
        
        return True


# First approach
# class Solution:
#     def isPalindrome(self, s: str) -> bool:

#         # O(n) solution

#         alphanumeric = set('abcdefghijklmnopqrstuvwxyz1234567890')
        
#         cleaned_s = ''
#         for c in s:
#             if c.lower() in alphanumeric:
#                 cleaned_s += c.lower()
        
#         return cleaned_s == cleaned_s[::-1]