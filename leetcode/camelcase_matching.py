# https://leetcode.com/problems/camelcase-matching


import re


class Solution:
    def camelMatch(self, queries: list[str], pattern: str) -> list[bool]:
        regex: str = "^[a-z]*"
        index: int = 0

        while index < len(pattern):
            regex += pattern[index] + "[a-z]*"
            index += 1
            while index < len(pattern) and ord(pattern[index]) > 91:
                regex += pattern[index] + "[a-z]*"
                index += 1

        regex += "$"

        result: list[bool] = []
        for q in queries:
            result.append(re.search(regex, q) is not None)

        return result
