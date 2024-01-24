# https://leetcode.com/problems/maximum-number-of-words-you-can-type


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken: dict[str, bool] = {}
        words: int = 0
        can_type: bool = True

        for i in brokenLetters:
            broken[i] = True

        for word in text.split():
            can_type = True
            for i in word:
                if broken.get(i, False):
                    can_type = False
                    break
            if can_type:
                words += 1

        return words
