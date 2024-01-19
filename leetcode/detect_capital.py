# https://leetcode.com/problems/detect-capital/


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) < 2:
            return True

        if word[0].islower() and word[1].isupper():
            return False

        expect_capital: bool = word[0].isupper() and word[1].isupper()
        for i in range(2, len(word)):
            if (word[i].isupper() and not expect_capital) or (not word[i].isupper() and expect_capital):
                return False
        return True
