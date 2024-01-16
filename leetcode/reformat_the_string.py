# https://leetcode.com/problems/reformat-the-string/


class Solution:
    def reformat(self, s: str) -> str:
        digits: list[str] = []
        chars: list[str] = []

        for i in s:
            if i.isdigit():
                digits.append(i)
            else:
                chars.append(i)

        if abs(len(digits) - len(chars)) > 1:
            return ""

        output: str = ""
        first: list[str] = []
        second: list[str] = []
        if len(digits) > len(chars):
            first = digits
            second = chars
        else:
            first = chars
            second = digits

        if len(digits) == len(chars):
            output += second.pop(0)

        output += first.pop(0)

        while len(digits) > 0 and len(chars) > 0:
            output += second.pop(0)
            output += first.pop(0)

        return output
