# https://leetcode.com/problems/delete-characters-to-make-fancy-string


class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s

        i: int = 0
        while i <= len(s) - 3:
            if s[i] == s[i + 1] and s[i + 1] == s[i + 2]:
                s = s[: i + 1] + s[i + 2 :]  # noqa E203
            else:
                i += 1
        return s
