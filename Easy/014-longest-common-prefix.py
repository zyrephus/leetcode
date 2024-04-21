class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        min_len = min(len(s) for s in strs)
        for i in range(min_len):
            for j in range(1, len(strs)):
                if strs[j][i] != strs[0][i]:
                    return pre
            pre += strs[0][i]
        return pre
