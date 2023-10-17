# https://leetcode.com/problems/account-balance-after-rounded-purchase


class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        mod: int = (100 - purchaseAmount) % 10
        return 100 - purchaseAmount - (mod if mod < 6 else -(10 - mod))
