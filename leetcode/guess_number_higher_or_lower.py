# https://leetcode.com/problems/guess-number-higher-or-lower


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
def guess(num: int) -> int:
    return num  # actual api not provided


class Solution:
    def guessNumber(self, n: int) -> int:
        lo: int = 0
        hi: int = n
        mid: int = lo + int((hi - lo) / 2)
        result: int = 0
        while lo < hi:
            mid = lo + int((hi - lo) / 2)
            result = guess(mid)
            if result == 0:
                return mid
            if result < 0:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
