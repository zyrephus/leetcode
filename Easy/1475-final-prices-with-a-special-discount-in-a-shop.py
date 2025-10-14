class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        stack = []
        res = prices[:]

        for i in range(n - 1, -1, -1):
            while stack and stack[-1] > prices[i]:
                stack.pop()

            discount = 0
            if stack:
                discount = stack[-1]

            res[i] = prices[i] - discount
            stack.append(prices[i])

        return res
