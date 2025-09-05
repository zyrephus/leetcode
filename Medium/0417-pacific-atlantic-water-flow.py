class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        pac_start, atl_start = set(), set()
        
        # Preprocessing
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    pac_start.add((r, c))
                if r == ROWS - 1 or c == COLS - 1:
                    atl_start.add((r, c))
        
        def bfs(starts):
            q = deque(starts)
            seen = set(starts)

            while q:
                r, c = q.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        if (nr, nc) not in seen and heights[nr][nc] >= heights[r][c]:
                            seen.add((nr, nc))
                            q.append((nr, nc))
            
            return seen
        
        pac = bfs(pac_start)
        atl = bfs(atl_start)

        return list(pac & atl)
