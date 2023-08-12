# https://leetcode.com/problems/unique-morse-code-words


class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse_code: list[str] = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
        unique: set[str] = set()

        for w in words:
            morse: str = ""
            for c in w:
                morse += morse_code[ord(c) - 97]
            unique.add(morse)

        return len(unique)
