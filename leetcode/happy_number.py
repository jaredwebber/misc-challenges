# https://leetcode.com/problems/happy-number


class Solution:
    def isHappy(self, n: int) -> bool:
        seen: set[int] = set()

        while n not in seen:
            seen.add(n)

            new_n: int = 0
            for i in str(n):
                val: int = int(i)
                new_n += val**2

            if new_n == 1:
                return True
            n = new_n

        return False
