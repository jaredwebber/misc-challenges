# https://leetcode.com/problems/first-letter-to-appear-twice


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen: set[str] = set()
        for i in s:
            if i in seen:
                return i
            seen.add(i)
        return ""
