# https://leetcode.com/problems/find-the-pivot-integer


class Solution:
    def pivotInteger(self, n: int) -> int:
        high: int = n
        low: int = 1
        count: int = 1
        while n > 0:
            if low == high and count == n:
                return count
            elif low < high:
                count += 1
                low += count
            else:
                n = n - 1
                high += n
        return -1
