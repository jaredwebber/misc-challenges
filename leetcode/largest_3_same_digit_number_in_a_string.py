# https://leetcode.com/problems/largest-3-same-digit-number-in-string


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest: int = -1
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] and num[i + 1] == num[i + 2]:
                largest = max(largest, int(num[i : i + 3]))  # noqa
        return str(largest) if largest > 0 else "000" if largest == 0 else ""
