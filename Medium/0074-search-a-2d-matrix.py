class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(log n) solution

        m, n = len(matrix), len(matrix[0])

        low, high = 0, m * n - 1

        while low <= high:
            mid = (low + high) // 2
            i = mid // n
            j = mid % n

            mid_num = matrix[i][j]

            if mid_num < target:
                low = mid + 1
            elif mid_num > target:
                high = mid - 1
            else:
                return True
        
        return False