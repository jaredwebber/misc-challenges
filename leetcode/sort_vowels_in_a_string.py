# https://leetcode.com/problems/sort-vowels-in-a-string


class Solution:
    def sortVowels(self, s: str) -> str:
        vowels: list[str] = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
        vowels_seen: list[str] = []

        for i in s:
            if i in vowels:
                vowels_seen.append(i)

        if len(vowels_seen) == 0:
            return s

        vowels_seen.sort()

        new_s: str = ""
        for i in range(len(s)):
            if s[i] in vowels:
                new_s += vowels_seen.pop(0)
            else:
                new_s += s[i]

        return new_s
