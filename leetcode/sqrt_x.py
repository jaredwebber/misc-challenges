# https://leetcode.com/problems/sqrtx


class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        num: int = 1
        sqrt: int = 1
        while sqrt <= x:
            num += 1
            sqrt = num * num

        return num - 1
