# https://leetcode.com/problems/count-symmetric-integers


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count: int = 0
        for i in range(low, high + 1):
            i_str: str = str(i)
            length: int = len(i_str)
            left: int = 0
            right: int = 0
            if length % 2 == 0:
                for c in range(length // 2):
                    left += int(i_str[c])
                    right += int(i_str[length - 1 - c])
                if left == right:
                    count += 1
        return count
