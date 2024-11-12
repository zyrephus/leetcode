class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # O(log n) solution

        low, high = 1, num

        while low <= high:
            mid = (low + high) // 2

            if mid * mid < num:
                low = mid + 1
            elif mid * mid > num: 
                high = mid - 1
            else:
                return True
        
        return False