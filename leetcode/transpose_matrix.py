# https://leetcode.com/problems/transpose-matrix


class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        updated_matrix: list[list[int]] = [[[0] for _ in range(len(matrix))] for _ in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                updated_matrix[j][i] = matrix[i][j]

        return updated_matrix
