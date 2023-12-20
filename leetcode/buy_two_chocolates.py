# https://leetcode.com/problems/buy-two-chocolates


class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        two_smallest: list[int] = [100, 100]
        for i in prices:
            if i < two_smallest[0]:
                two_smallest[1] = two_smallest[0]
                two_smallest[0] = i
            elif i < two_smallest[1]:
                two_smallest[1] = i

        return money if sum(two_smallest) > money else money - sum(two_smallest)

    # shorter approach requiring sorting
    def buyChoco_alt(self, prices: list[int], money: int) -> int:
        prices.sort()
        return money - prices[0] - prices[1] if money - prices[0] - prices[1] >= 0 else money
