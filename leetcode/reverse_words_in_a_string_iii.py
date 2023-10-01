# https://leetcode.com/problems/reverse-words-in-a-string-iii


class Solution:
    def reverseWords(self, s: str) -> str:
        out: str = ""
        for word in s.split():
            for c in range(len(word) - 1, -1, -1):
                out += word[c]
            out += " "
        return out.rstrip()
