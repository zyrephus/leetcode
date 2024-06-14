class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}
        for i in range(len(s)):
            if s[i] in s_map:
                s_map[s[i]] += 1
            elif s[i] not in s_map:
                s_map[s[i]] = 1
            if t[i] in t_map:
                t_map[t[i]] += 1
            elif t[i] not in t_map:
                t_map[t[i]] = 1
        for char in s_map:
            if s_map[char] != t_map.get(char, 0):
                return False
        return True