class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]

        res = 0

        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                res += l_max - height[l] # Never going to be < 0
            else:
                r -= 1
                r_max = max(r_max, height[r])
                res += r_max - height[r] # Never going to be < 0
            
        return res
