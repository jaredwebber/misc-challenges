# https://leetcode.com/problems/backspace-string-compare


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_out: str = ""
        for i in s:
            if i == "#":
                s_out = s_out[:-1]
            else:
                s_out += i

        t_out: str = ""
        for i in t:
            if i == "#":
                t_out = t_out[:-1]
            else:
                t_out += i

        return s_out == t_out
