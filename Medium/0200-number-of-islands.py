class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(sr, sc):
            q = deque([(sr, sc)])
            grid[sr][sc] = '0'

            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'
                        q.append((nr, nc))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    res += 1
                    bfs(r, c)

        return res
        
