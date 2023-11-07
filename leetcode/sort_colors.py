# https://leetcode.com/problems/sort-colors


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts: dict[int, int] = {}
        for i in nums:
            counts[i] = counts.get(i, 0) + 1

        index: int = 0
        for i in range(0, 3):
            if counts.get(i):
                for j in range(counts.get(i)):
                    nums[index] = i
                    index += 1
