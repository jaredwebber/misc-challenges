# https://leetcode.com/problems/keyboard-row


class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        rows = ["qwertyuiopQWERTYUIOP", "asdfghjklASDFGHJKL", "zxcvbnmZXCVBNM"]
        row = 0
        can_type = []

        for word in words:
            row = 2 if word[0] in rows[2] else 1 if word[0] in rows[1] else 0
            single_row = True
            for i in range(1, len(word)):
                if word[i] not in rows[row]:
                    single_row = False
                    break
            if single_row:
                can_type.append(word)

        return can_type
