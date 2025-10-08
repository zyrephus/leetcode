class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = { u: [] for u in range(1, n + 1) }
        for u, v, t in times:
            adj[u].append([v, t])

        visited = set()
        minHeap = [[0, k]]
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if n1 in visited:
                continue

            visited.add(n1)
            t = w1

            # BFS
            for n2, w2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w2 + w1, n2))

        return t if len(visited) == n else -1
