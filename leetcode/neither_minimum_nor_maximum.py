# https://leetcode.com/problems/neither-minimum-nor-maximum


class Solution:
    def findNonMinOrMax(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return -1

        low: int = 101
        hi: int = -1
        for i in nums:
            if i < low:
                low = i
            if i > hi:
                hi = i

        for i in nums:
            if i != low and i != hi:
                return i

        return -1
