# https://leetcode.com/problems/valid-perfect-square


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(num + 1):
            res: int = i * i
            if res == num:
                return True
            if res > num:
                return False

        return False
