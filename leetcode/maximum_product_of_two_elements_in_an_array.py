# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if len(nums) > 2:
            nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)
