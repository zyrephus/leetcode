class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # O(n) solution
        
        res = ""

        length = min(len(word1), len(word2))
        for i in range(length):
            toAdd = word1[i] + word2[i]
            res += toAdd

        longestWord = longestWord = word1 if len(word1) > len(word2) else word2
        res += longestWord[length::]
        
        return res