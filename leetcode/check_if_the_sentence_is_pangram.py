# https://leetcode.com/problems/check-if-the-sentence-is-pangram


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        unique: set[str] = set()
        for i in sentence:
            unique.add(i)
            if len(unique) == 26:
                return True
        return False
