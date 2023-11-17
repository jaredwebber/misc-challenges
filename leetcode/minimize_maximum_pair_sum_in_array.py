# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array


class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        max_pair: int = 0
        for i in range(len(nums) // 2):
            max_pair = max(max_pair, nums[i] + nums[len(nums) - 1 - i])
        return max_pair
