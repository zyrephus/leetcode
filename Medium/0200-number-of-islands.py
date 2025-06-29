class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        res = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            queue = deque([(r, c)])
            visited.add((r, c))

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    curr_dr = row + dr
                    curr_dc = col + dc
                    if (curr_dr) in range(ROWS) and (curr_dc) in range(COLS) and grid[curr_dr][curr_dc] == "1" and (curr_dr, curr_dc) not in visited:
                        queue.append((curr_dr, curr_dc))
                        visited.add((curr_dr, curr_dc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    res += 1

        return res
