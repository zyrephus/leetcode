class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        DIRS = {
            'U': (-1, 0),
            'D': (1, 0),
            'L': (0, -1),
            'R': (0, 1),
        }

        res = []

        for i in range(len(s)):
            r, c = startPos

            count = 0
            for j in range(i, len(s)):
                dr, dc = DIRS[s[j]]
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n:
                    count += 1
                    r, c = nr, nc
                else:
                    break
            
            res.append(count)

        return res
