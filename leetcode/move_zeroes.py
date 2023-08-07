# https://leetcode.com/problems/move-zeroes


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index: int = 0
        zeroes: int = 0
        while index < len(nums) - zeroes:
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
                zeroes += 1
            else:
                index += 1
