# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix


class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        counts: list[list[int]] = []
        for i in range(len(mat)):
            curr: list[int] = [i, 0]
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    curr[1] += 1
            counts.append(curr)

        counts.sort(key=lambda x: x[1])

        k_weakest: list[int] = []
        for i in range(k):
            k_weakest.append(counts[i][0])

        return k_weakest
