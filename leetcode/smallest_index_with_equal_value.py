# https://leetcode.com/problems/smallest-index-with-equal-value/


class Solution:
    def smallestEqual(self, nums: list[int]) -> int:
        for index, val in enumerate(nums):
            if index % 10 == val:
                return index
        return -1
