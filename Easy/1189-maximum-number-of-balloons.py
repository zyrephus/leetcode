# Optimized solution:
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # O(n) solution

        counter = defaultdict(int)
        balloon = 'balloon'

        for c in text:
            if c in balloon:
                counter[c] += 1
        
        # Checks if any characters in balloon aren't in counter
        if any(c not in counter for c in balloon):
            return 0
        else:
            return min(counter['b'], counter['a'], counter['l'] // 2, counter['o'] // 2, counter['n'])

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
