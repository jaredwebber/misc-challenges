# https://leetcode.com/problems/first-unique-character-in-a-string/description/


class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique: dict[str, int] = {}
        for i in range(len(s)):
            if unique.get(s[i]) is not None:
                unique[s[i]] = -1
            else:
                unique[s[i]] = i

        for _, v in unique.items():
            if v >= 0:
                return v
        return -1
