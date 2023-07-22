# https://leetcode.com/problems/count-asterisks


class Solution:
    def countAsterisks(self, s: str) -> int:
        inPair: bool = False
        count: int = 0
        for i in s:
            if i == "|":
                inPair = not inPair
            elif i == "*" and not inPair:
                count += 1
        return count


class AlternateSolution:
    def countAsterisks(self, s: str) -> int:
        count: int = 0
        tokens: list[str] = s.split("|")
        for i in range(0, len(tokens), 2):
            for c in tokens[i]:
                if c == "*":
                    count += 1
        return count
