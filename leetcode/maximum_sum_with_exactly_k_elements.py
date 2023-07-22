# https://leetcode.com/problems/maximum-sum-with-exactly-k-elements


class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        maximum: int = 0
        for i in nums:
            maximum = max(maximum, i)

        for i in range(maximum + 1, maximum + k):
            maximum += i

        return maximum
