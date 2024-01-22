# https://leetcode.com/problems/set-mismatch


class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        nums.sort()

        total: int = nums[0]
        expected: int = 1
        duplicate: int = -1

        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                duplicate = nums[i]
            total += nums[i]
            expected += i + 1

        return [duplicate, expected - (total - duplicate)]
