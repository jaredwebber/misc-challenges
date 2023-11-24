# https://leetcode.com/problems/maximum-number-of-coins-you-can-get


class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()

        count: int = 0
        me: int = len(piles) - 2
        bob: int = 0

        while me > bob:
            count += piles[me]
            me -= 2
            bob += 1

        return count
