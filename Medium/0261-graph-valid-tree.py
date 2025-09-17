class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        
        adj = { v: [] for v in range(n) }
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(u, parent):
            visited.add(u)

            for v in adj[u]:
                if v == parent:
                    continue
                if v in visited:
                    return False # Cycle
                if not dfs(v, u):
                    return False
            
            return True

        return dfs(0, -1) and len(visited) == n
