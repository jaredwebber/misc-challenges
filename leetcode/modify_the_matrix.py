# https://leetcode.com/problems/modify-the-matrix


class Solution:
    def modifiedMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        mappings: dict[int, list[int]] = {}
        col_max: dict[int, int] = {}

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == -1:
                    if mappings.get(j):
                        mappings[j].append(i)
                    else:
                        mappings[j] = [i]
                else:
                    col_max[j] = max(col_max.get(j, 0), matrix[i][j])

        for col, replacements in mappings.items():
            for row in replacements:
                matrix[row][col] = col_max.get(col)

        return matrix
