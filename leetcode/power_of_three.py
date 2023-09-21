# https://leetcode.com/problems/power-of-three


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 59049:  # 3^{10}
            n = n / 59049

        while n >= 3:
            n = n / 3

        return n == 1
