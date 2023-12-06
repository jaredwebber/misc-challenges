# https://leetcode.com/problems/calculate-money-in-leetcode-bank


class Solution:
    def totalMoney(self, n: int) -> int:
        count: int = 0
        weeks: int = n // 7

        for i in range(weeks):
            count += 28 + (i * 7)

        for i in range(n % 7):
            count += weeks + 1 + i

        return count
