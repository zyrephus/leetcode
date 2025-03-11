class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)

        if len_s1 > len_s2:
            return False

        f_s1, f_s2 = [0] * 26, [0] * 26

        for i in range(len_s1):
            # 97 = ord('a')
            f_s1[ord(s1[i]) - 97] += 1
            f_s2[ord(s2[i]) - 97] += 1
        
        if f_s1 == f_s2:
            return True
        
        for i in range(len_s1, len_s2):
            f_s2[ord(s2[i]) - 97] += 1
            f_s2[ord(s2[i - len_s1]) - 97] -= 1

            if f_s1 == f_s2:
                return True

        return False
      
