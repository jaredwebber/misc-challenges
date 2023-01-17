# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_prev: int = 1000000
        max_profit: int = 0
        for i in prices:
            max_profit = max(max_profit, (i - min_prev))
            min_prev = min(min_prev, i)

        return max_profit
