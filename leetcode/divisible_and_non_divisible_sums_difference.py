# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        non: int = 0
        divisible: int = 0

        for i in range(1, n + 1):
            if i % m == 0:
                divisible += i
            else:
                non += i
        return non - divisible
