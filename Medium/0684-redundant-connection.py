class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range (n + 1)] # ith node -> parent 
        rank = [1] * (n + 1)

        def find(u):
            if u != parent[u]:
                parent[u] = find(parent[u])

            return parent[u]

        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return False

            if rank[pu] > rank[pv]:
                parent[pv] = pu
                rank[pu] += rank[pv]
            else:
                parent[pu] = parent[pv]
                rank[pv] += rank[pu]

            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
                
