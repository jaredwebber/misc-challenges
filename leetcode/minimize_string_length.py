# https://leetcode.com/problems/minimize-string-length


class Solution:
    def minimizedStringLength(self, s: str) -> int:
        letters: set[str] = set()
        for i in s:
            letters.add(i)
        return len(letters)
