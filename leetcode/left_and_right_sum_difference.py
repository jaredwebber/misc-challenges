# https://leetcode.com/problems/left-and-right-sum-differences


class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        sums: list[int] = [0 for i in range(len(nums))]

        for i in range(len(nums)):
            sums[i] = 0 if i == 0 else (sums[i - 1] + nums[i - 1])

        for i in range(len(sums)):
            sums[i] = abs(
                sums[i] - (0 if i == 0 else (sums[len(nums) - i] + nums[len(nums) - i]))
            )

        return sums
