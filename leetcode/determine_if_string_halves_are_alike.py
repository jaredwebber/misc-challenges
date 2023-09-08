# https://leetcode.com/problems/determine-if-string-halves-are-alike


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels: list[str] = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        first_half: int = 0
        second_half: int = 0
        for i in range(len(s) // 2):
            first_half += 1 if s[i] in vowels else 0
            second_half += 1 if s[len(s) - 1 - i] in vowels else 0

        return first_half == second_half
