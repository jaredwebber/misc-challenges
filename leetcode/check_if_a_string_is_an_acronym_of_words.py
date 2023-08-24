# https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words


class Solution:
    def isAcronym(self, words: list[str], s: str) -> bool:
        if len(words) != len(s):
            return False

        for i in range(len(s)):
            if s[i] != words[i][0]:
                return False
        return True
