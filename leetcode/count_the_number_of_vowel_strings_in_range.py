# https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range


class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        vowels: list[str] = ["a", "e", "i", "o", "u"]
        vowel_strings: int = 0

        for i in range(left, right + 1):
            if words[i][0] in vowels and words[i][-1] in vowels:
                vowel_strings += 1
        return vowel_strings
