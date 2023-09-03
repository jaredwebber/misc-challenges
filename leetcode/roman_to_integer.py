# https://leetcode.com/problems/roman-to-integer


class Solution:
    def romanToInt(self, s: str) -> int:
        num: int = 0
        val_map: dict[str, int] = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }
        index: int = 0

        while index < len(s):
            if index < len(s) - 1 and val_map.get(s[index] + s[index + 1]) is not None:
                num += val_map.get(s[index] + s[index + 1])
                index += 1
            else:
                num += val_map.get(s[index])
            index += 1

        return num
