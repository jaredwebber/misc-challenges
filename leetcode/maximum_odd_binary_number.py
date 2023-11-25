# https://leetcode.com/problems/maximum-odd-binary-number


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones: int = s.count("1") - 1
        return ("1" * ones) + ((len(s) - 1 - ones) * "0") + "1"
