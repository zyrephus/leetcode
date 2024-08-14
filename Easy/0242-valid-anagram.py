class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(n) solution

        if len(s) != len(t):
            return False

        freq_s = {}
        for c in s:
            freq_s[c] = 1 + freq_s.get(c, 0)
        
        freq_t = {}
        for c in t:
            freq_t[c] = 1 + freq_t.get(c, 0)
        
        return freq_t == freq_s
    
        # Another approach
        # if len(s) != len(t):
        #     return False
        # s_map = {}
        # t_map = {}
        # for i in range(len(s)):
        #     if s[i] in s_map:
        #         s_map[s[i]] += 1
        #     elif s[i] not in s_map:
        #         s_map[s[i]] = 1
        #     if t[i] in t_map:
        #         t_map[t[i]] += 1
        #     elif t[i] not in t_map:
        #         t_map[t[i]] = 1
        # for char in s_map:
        #     if s_map[char] != t_map.get(char, 0):
        #         return False
        # return True