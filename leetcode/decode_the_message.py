# https://leetcode.com/problems/decode-the-message


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        char_set: set[str] = set()
        char_map: dict[str, str] = {}
        for i in key:
            if i.isalpha():
                if i not in char_set:
                    char_set.add(i)
                    char_map[i] = chr(97 + len(char_map))
            if len(char_set) == 26:
                break

        decoded: str = ""
        for i in message:
            if i.isalpha():
                decoded += char_map.get(i)
            else:
                decoded += i

        return decoded
