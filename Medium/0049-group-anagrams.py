class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) # frequency -> list of strings

        for s in strs:
            # Get frequency
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord("a")] += 1

            groups[tuple(freq)].append(s)

        return list(groups.values())
