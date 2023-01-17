# https://leetcode.com/problems/two-sum/


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int] = {}
        for i in range(len(nums)):
            if seen.get(target - nums[i]) is not None:
                return [seen.get(target - nums[i]), i]
            seen[nums[i]] = i
        return []
