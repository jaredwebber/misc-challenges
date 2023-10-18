# https://leetcode.com/problems/row-with-maximum-ones/description/


class Solution:
    def rowAndMaximumOnes(self, mat: list[list[int]]) -> list[int]:
        row_maxones: list[int] = [0, 0]
        curr: int = 0

        for i in range(len(mat)):
            curr = sum(mat[i])
            if curr > row_maxones[1]:
                row_maxones = [i, curr]
        return row_maxones
