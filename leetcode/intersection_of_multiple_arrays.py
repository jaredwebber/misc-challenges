# https://leetcode.com/problems/intersection-of-multiple-arrays


class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        intersect: set[int] = set(nums[0])
        for i in range(1, len(nums)):
            intersect = intersect.intersection(nums[i])

        return sorted(list(intersect))
