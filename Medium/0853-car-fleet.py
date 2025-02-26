class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)] # List of [position, speed]
        pair = sorted(pair, reverse=True) # Sorted in reverse order and exclude first element
        
        res = 1
        
        curr_fleet = (target - pair[0][0]) / pair[0][1]
        for p, s in pair[1:]:
            curr_car = (target - p) / s

            if curr_fleet < curr_car:
                res += 1
                curr_fleet = curr_car

        return res
