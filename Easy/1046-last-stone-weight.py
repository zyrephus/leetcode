class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-n for n in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -heapq.heappop(stones) # Largest
            x = -heapq.heappop(stones) # Second largest

            if x != y:
                heapq.heappush(stones, -(y - x))
            
        return -stones[0] if stones else 0
