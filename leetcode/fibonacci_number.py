# https://leetcode.com/problems/fibonacci-number/


class Solution:
    def fib(self, n: int) -> int:
        prev: int = 0
        curr: int = 1
        next_val: int = 0

        if n < 2:
            return n

        for _ in range(2, n + 1):
            next_val = prev + curr
            prev = curr
            curr = next_val

        return curr
