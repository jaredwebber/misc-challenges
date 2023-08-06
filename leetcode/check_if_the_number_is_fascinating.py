# https://leetcode.com/problems/check-if-the-number-is-fascinating


class Solution:
    def isFascinating(self, n: int) -> bool:
        num: str = str(n) + str(2 * n) + str(3 * n)
        if (
            len(num) != 9
            or "1" not in num
            or "2" not in num
            or "3" not in num
            or "4" not in num
            or "5" not in num
            or "6" not in num
            or "7" not in num
            or "8" not in num
            or "9" not in num
        ):
            return False
        return True
