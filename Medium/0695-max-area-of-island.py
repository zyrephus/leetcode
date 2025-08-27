class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(sr, sc):
            q = deque([(sr, sc)])

            grid[sr][sc] = 0
            curr_area = 1

            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        curr_area += 1
                        q.append((nr, nc))

            return curr_area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs(r, c))

        return max_area
