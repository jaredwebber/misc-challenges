# https://leetcode.com/problems/number-of-1-bits


class Solution:
    def hammingWeight(self, n: int) -> int:
        count: int = 0
        for i in bin(n):
            if i == "1":
                count += 1
        return count
