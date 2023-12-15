# https://leetcode.com/problems/find-words-containing-character


class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        results: list[int] = []
        for i, word in enumerate(words):
            if x in word:
                results.append(i)
        return results
