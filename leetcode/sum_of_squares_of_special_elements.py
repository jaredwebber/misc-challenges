# https://leetcode.com/problems/sum-of-squares-of-special-elements


class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        total: int = 0
        length: int = len(nums)
        for i in range(1, length + 1):
            if length % i == 0:
                total += nums[i - 1] * nums[i - 1]
        return total
