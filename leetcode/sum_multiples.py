# https://leetcode.com/problems/sum-multiples


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        multiple_sum: int = 0
        for i in range(3, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                multiple_sum += i
        return multiple_sum
