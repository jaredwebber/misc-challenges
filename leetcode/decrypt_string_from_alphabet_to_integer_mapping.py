# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping


class Solution:
    def get_ascii(self, s: str) -> str:
        return chr(int(s) + 96)

    def freqAlphabets(self, s: str) -> str:
        out: str = ""
        elements: list[str] = s.split("#")

        for i in range(len(elements)):
            element_len: int = len(elements[i])
            if element_len > 0:
                if i == len(elements) - 1:
                    if s[len(s) - 1] == "#":
                        out += self.get_ascii(elements[i])
                    else:
                        for c in elements[i]:
                            out += self.get_ascii(c)
                else:
                    if len(elements[i]) <= 2:
                        out += self.get_ascii(elements[i])
                    else:
                        for c in range(element_len - 2):
                            out += self.get_ascii(elements[i][c])
                        out += self.get_ascii(elements[i][element_len - 2] + elements[i][element_len - 1])
        return out
