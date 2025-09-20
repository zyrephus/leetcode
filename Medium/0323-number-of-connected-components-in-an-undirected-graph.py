class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = 0

        seen = set()

        adj = { u: [] for u in range(n) }
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def bfs(u):
            q = deque([u])
            seen.add(u)

            while q:
                curr = q.popleft()
                for v in adj[curr]:
                    if v not in seen:
                        seen.add(v)
                        q.append(v)

        for u in range(n):
            if u not in seen:
                components += 1
                bfs(u)
        
        return components
