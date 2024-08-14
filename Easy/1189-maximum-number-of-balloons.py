class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # O(n) solution

        balloon = {
            "b": 0,
            "a": 0,
            "l": 0,
            "o": 0,
            "n": 0
        }

        # Getting the count of all the letters in balloon in text
        for c in text:
            if c in balloon:
                balloon[c] += 1
        
        # Finding how many instances of balloon there is
        balloon["l"] //= 2
        balloon["o"] //= 2
        
        return min(balloon["b"], balloon["a"], balloon["l"], balloon["o"], balloon["n"])

# First solution:
# class Solution:
#     def maxNumberOfBalloons(self, text: str) -> int:
#         # O(n) solution

#         stack = list(text)
#         balloon_dict = {
#             'b': 0,
#             'a': 0,
#             'l': 0,
#             'o': 0,
#             'n': 0
#         }

#         for char in range(len(stack) - 1, -1, -1):
#             if stack[char] in balloon_dict:
#                 balloon_dict[stack[char]] += 1
        
#         count = 0
#         while True:
#             if balloon_dict['b'] != 0 and balloon_dict['a'] != 0 and balloon_dict['n'] != 0:
#                 if (balloon_dict['l'] != 0 and balloon_dict['l'] > 1) and (balloon_dict['o'] != 0 and balloon_dict['o'] > 1):
#                         balloon_dict['b'] -= 1
#                         balloon_dict['a'] -= 1
#                         balloon_dict['n'] -= 1
#                         balloon_dict['l'] -= 2
#                         balloon_dict['o'] -= 2
#                         count += 1
#             if balloon_dict['b'] == 0 or balloon_dict['a'] == 0 or balloon_dict['n'] == 0 or balloon_dict['l'] < 2 or balloon_dict['o'] < 2:
#                 break
        
#         return count
