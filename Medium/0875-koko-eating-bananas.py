class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = 1
        left, right = 1, max(piles)

        while left <= right:
            mid = (left + right) // 2

            # Loop over piles
            total = 0
            for pile in piles:
                total += math.ceil(pile / mid)
            
            # Eating too much
            if total <= h:
                res = mid
                right = mid - 1
            # Eating too less
            else:
                left = mid + 1

        return res

        
