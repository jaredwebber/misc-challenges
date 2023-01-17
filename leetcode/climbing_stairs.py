# https://leetcode.com/problems/climbing-stairs/description/


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        one: int = 3
        two: int = 2

        for i in range(3, n):
            if i % 2 == 0:
                one += two
            else:
                two += one

        return max(one, two)
