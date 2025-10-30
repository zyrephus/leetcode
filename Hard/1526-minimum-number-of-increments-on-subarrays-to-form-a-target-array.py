class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = prev = target[0]
        for i in range(1, len(target)):
            if prev < target[i]:
                res += (target[i] - prev)
            
            prev = target[i]

        return res
