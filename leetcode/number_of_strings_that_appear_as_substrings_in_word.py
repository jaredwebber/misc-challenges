# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word


class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        count: int = 0
        for i in patterns:
            if i in word:
                count += 1
        return count
