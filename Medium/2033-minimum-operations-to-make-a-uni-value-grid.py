class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flattened = [num for row in grid for num in row] # Flatten grid

        # Check modulo condition
        mod = flattened[0] % x
        for num in flattened:
            if num % x != mod:
                return -1

        # Calculate moves
        flattened.sort()
        mid = flattened[len(flattened) // 2]
        moves = 0
        for num in flattened:
            moves += abs(num - mid) // x
        
        return moves

