class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        maxProfit = 0
        left = 0
        right = 1

        while left < right and right < len(prices):
            buy = prices[left]
            sell = prices[right]

            if buy >= sell:
                left += 1
                if left == right:
                    right += 1
            else:
                maxProfit = max(maxProfit, sell - buy)
                right += 1

        return maxProfit
