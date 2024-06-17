class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # O(n + m) solution

        s = set(jewels) # ('a', 'A')
        count = 0

        for stone in stones:
            # Constant time lookup for sets
            if stone in s:
                count += 1
        
        return count