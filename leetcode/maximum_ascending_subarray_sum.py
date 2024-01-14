# https://leetcode.com/problems/maximum-ascending-subarray-sum


class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        max_sum: int = nums[0]
        curr_sum: int = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr_sum += nums[i]
            else:
                max_sum = max(curr_sum, max_sum)
                curr_sum = nums[i]
        return max(curr_sum, max_sum)
