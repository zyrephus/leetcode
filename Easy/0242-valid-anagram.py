class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s, len_t = len(s), len(t)

        if len_s != len_t:
            return False
        
        count = [0] * 26

        for i in range(len_s):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for c in count:
            if c != 0:
                return False
        return True
    
        # Another approach
        # len_s, len_t = len(s), len(t)

        #  if len_s != len_t:
        #      return False
        
        #  s_freq = {}
        #  t_freq = {}

        #  for i in range(len_s):
        #      s_freq[s[i]] = 1 + s_freq.get(s[i], 0)
        #      t_freq[t[i]] = 1 + t_freq.get(t[i], 0)
        
        #  return s_freq == t_freq
        
