# https://leetcode.com/problems/rearrange-spaces-between-words/


class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces: int = text.count(" ")

        if spaces == 0:
            return text

        words: list[str] = text.split()

        if len(words) == 1:
            return words[0] + (" " * spaces)

        output: str = ""

        for i in range(len(words)):
            output += words[i]
            if i < len(words) - 1:
                output += " " * (spaces // (len(words) - 1))

        if spaces % (len(words) - 1) != 0:
            output += " " * (spaces % (len(words) - 1))

        return output
