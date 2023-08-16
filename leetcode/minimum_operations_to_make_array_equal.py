# https://leetcode.com/problems/minimum-operations-to-make-array-equal


class Solution:
    def minOperations(self, n: int) -> int:
        if n < 3:
            return n - 1
        ops: int = 2
        increment: int = 2
        for i in range(3, n):
            ops += increment
            if i % 2 == 0:
                increment += 1
        return ops


"""
1: 0
2: 1
3: 2
4: 4
5: 6
6: 9
7: 12
8: 16
9: 20
10: 25
11: 30
12: 36
13: 42
14: 49
"""
