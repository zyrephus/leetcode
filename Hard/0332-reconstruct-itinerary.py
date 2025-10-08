class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for u, v in tickets:
            adj[u].append(v)

        # Sort in reverse so we can always pop smallest
        for u in adj:
            adj[u].sort(reverse=True)

        route = []
        stack = ["JFK"]

        while stack:
            u = stack[-1]
            if adj[u]:
                stack.append(adj[u].pop()) # Consume next smallest edge
            else:
                route.append(stack.pop()) # Dead end, add to route

        route.reverse()
        return route
