# https://leetcode.com/problems/faulty-keyboard


class Solution:
    def finalString(self, s: str) -> str:
        out: str = ""
        for i in s:
            if i == "i":
                out = out[::-1]
            else:
                out += i

        return out
