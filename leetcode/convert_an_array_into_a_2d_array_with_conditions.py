# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions


class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        matrix: list[list[int]] = []
        elements_counted: int = 0

        while elements_counted < len(nums):
            row: list[int] = []
            for i in range(len(nums)):
                if nums[i] != -1 and nums[i] not in row:
                    row.append(nums[i])
                    nums[i] = -1
                    elements_counted += 1
            matrix.append(row)

        return matrix
