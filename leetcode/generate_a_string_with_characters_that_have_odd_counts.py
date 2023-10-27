# https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts


class Solution:
    def generateTheString(self, n: int) -> str:
        return "a" * (n - 1) + ("a" if n % 2 != 0 else "b")
