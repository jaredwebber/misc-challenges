# https://leetcode.com/problems/special-positions-in-a-binary-matrix


class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        rows: list[int] = [0 for _ in range(len(mat))]
        cols: list[int] = [0 for _ in range(len(mat[0]))]
        count: int = 0

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1

        for i in range(len(rows)):
            if rows[i] == 1:
                if cols[mat[i].index(1)] == 1:
                    count += 1

        return count
