# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array


class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        element_sum: int = 0
        digit_sum: int = 0
        for i in nums:
            for d in str(i):
                digit_sum += int(d)
            element_sum += i
        return abs(element_sum - digit_sum)
