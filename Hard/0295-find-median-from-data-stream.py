class MedianFinder:
    def __init__(self):
        self.max_heap = [] # Left side
        self.min_heap = [] # Right side

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        
        # Move largest from max_heap to min_heap
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # Ensure max_heap can have 1 more element than min_heap
        if (len(self.min_heap) > len(self.max_heap)):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        
    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
