# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array


class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        count: int = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and ((i * j) % k) == 0:
                    count += 1

        return count
