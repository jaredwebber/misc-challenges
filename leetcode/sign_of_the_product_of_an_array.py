# https://leetcode.com/problems/sign-of-the-product-of-an-array


class Solution:
    def arraySign(self, nums: list[int]) -> int:
        negative: bool = False
        for i in nums:
            if i < 0:
                negative = not negative
            elif i == 0:
                return 0

        return -1 if negative else 1
