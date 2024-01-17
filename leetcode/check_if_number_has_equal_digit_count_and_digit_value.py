# https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value


class Solution:
    def digitCount(self, num: str) -> bool:
        digit_map: dict[int, int] = {}
        for i in num:
            digit_map[i] = digit_map.get(i, 0) + 1

        print(digit_map)
        for i in range(len(num)):
            if digit_map.get(str(i), 0) != int(num[i]):
                return False

        return True
