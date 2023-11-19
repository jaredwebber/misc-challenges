# https://leetcode.com/problems/removing-stars-from-a-string


class Solution:
    def removeStars(self, s: str) -> str:
        out: str = ""
        remove: int = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "*":
                remove += 1
            elif remove > 0:
                remove -= 1
            else:
                out += s[i]

        return out[::-1]
