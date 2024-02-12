# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero


class Solution:
    def sumZero(self, n: int) -> list[int]:
        vals: list[int] = [] if n % 2 == 0 else [0]

        for i in range(1, (n // 2) + 1):
            vals.append(i)
            vals.append(-i)

        return vals
