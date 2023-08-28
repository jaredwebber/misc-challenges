# https://leetcode.com/problems/max-pair-sum-in-an-array


class Solution:
    def maxSum(self, nums: list[int]) -> int:
        maximum_digit: dict[int, int] = {}
        max_sum: int = -1
        for i in nums:
            curr_max_digit: int = self.get_max_digit(i)
            if maximum_digit.get(curr_max_digit) is not None:
                max_sum = max(max_sum, maximum_digit.get(curr_max_digit) + i)
                maximum_digit[curr_max_digit] = max(
                    i, maximum_digit.get(curr_max_digit)
                )
            else:
                maximum_digit[curr_max_digit] = i
        return max_sum

    def get_max_digit(self, num: int) -> int:
        digit: int = -1
        for i in str(num):
            if int(i) > digit:
                digit = int(i)
        return digit
