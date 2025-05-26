class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            freq[task] = 1 + freq.get(task, 0)
        
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap) # O(26)

        time = 0
        q = deque() # Pairs of [-f, idle_time]

        while max_heap or q:
            time += 1

            if max_heap:
                count = 1 + heapq.heappop(max_heap)
                if count:
                    q.append([count, time + n])

            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

        return time
      
