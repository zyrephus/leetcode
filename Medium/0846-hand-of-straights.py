class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        # Get frequency
        freq = {}
        for num in hand:
            freq[num] = 1 + freq.get(num, 0)

        min_heap = list(freq.keys())
        heapq.heapify(min_heap)
        while min_heap:
            first = min_heap[0]
            for i in range(first, first + groupSize):
                if i not in freq:
                    return False
                  
                freq[i] -= 1
                if freq[i] == 0:
                    heapq.heappop(min_heap)

        return True 
        
