# https://leetcode.com/problems/minimum-operations-to-collect-elements


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        collection: set[int] = set()

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] <= k:
                collection.add(nums[i])
                if len(collection) == k:
                    return len(nums) - i
        return len(nums)
