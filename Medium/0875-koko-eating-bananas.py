class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # O(n * log(max(piles))) solution

        def k_works(k):
            hours = 0
            for pile in piles:
                hours += ceil(pile / k)
            
            return hours <= h
        
        left, right = 1, max(piles)

        while left < right:
            k = (left + right) // 2

            if k_works(k):
                right = k # k could still be minimum integer
            else:
             left = k + 1 # k is definitely not minimum integer
        
        return left # can also return right