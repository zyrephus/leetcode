class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n) solution

        if not prices:
            return 0
        
        left, right, profit = 0, 1, 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = max(profit, prices[right] - prices[left])
            else:
                left = right
            right += 1
        return profit
        
        # First approach

        # profit = 0
        # left, right = 0, 1

        # while right < len(prices):
        #     if prices[right] - prices[left] < 0:
        #         left = right
        #     else:
        #         profit = max(profit, prices[right] - prices[left])
        #     right += 1
        
        # return profit