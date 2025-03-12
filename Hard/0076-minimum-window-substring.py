class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        t_freq, window = {}, {}

        for c in t:
            t_freq[c] = 1 + t_freq.get(c, 0)

        have, need = 0, len(t_freq)

        res, res_len = [-1, -1], float("infinity")

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in t_freq and window[c] == t_freq[c]:
                have += 1

            while have == need:
                # Update result
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                
                # Pop from left of window
                window[s[l]] -= 1
                if s[l] in t_freq and window[s[l]] < t_freq[s[l]]:
                    have -= 1
                l += 1
        
        return s[res[0] : res[1] + 1] if res_len != float("infinity") else ""
