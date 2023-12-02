# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        char_map: dict[str, int] = {}
        total: int = 0

        for i in chars:
            char_map[i] = char_map.get(i, 0) + 1

        char: str = ""
        char_count: int = 1
        valid: bool = True
        for word in words:
            word = "".join(sorted(word))

            char = ""
            char_count = 0
            valid = True

            for i in word:
                if i == char:
                    char_count += 1
                else:
                    if char_map.get(char, 0) < char_count:
                        valid = False
                        break
                    char_count = 1
                    char = i

            if valid and char_map.get(word[0], 0) > 0 and char_map.get(char, 0) >= char_count:
                total += len(word)

        return total
