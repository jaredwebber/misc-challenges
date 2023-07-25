# https://leetcode.com/problems/replace-all-digits-with-characters


class Solution:
    def replaceDigits(self, s: str) -> str:
        replaced: str = ""
        for i in range(1, len(s), 2):
            replaced += s[i - 1] + chr(ord(s[i - 1]) + int(s[i]))
        return replaced if len(s) % 2 == 0 else replaced + s[len(s) - 1]
